from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec, PodSpec  
from langchain_pinecone import PineconeVectorStore
from langchain import hub
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
from nemoguardrails import LLMRails, RailsConfig
from nemoguardrails.integrations.langchain.runnable_rails import RunnableRails
import bs4
import os
import time
import asyncio

load_dotenv(find_dotenv())

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ['LANGCHAIN_PROJECT'] = 'end-to-end-rag'

class RAG:

    def __init__(self, web_url):
        
        self.vectorstore_index_name = "end-to-end-rag"
        self.loader = WebBaseLoader(
            web_paths=(web_url,),
            bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                    class_=("post-content", "post-title", "post-header")
                )
            ),
        )
        self.embeddings = OpenAIEmbeddings(
            api_key=os.getenv("OPENAI_API_KEY"), model="text-embedding-3-small"
        )
        self.groq_llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"), 
            model="llama3-70b-8192", 
            temperature=0
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000, 
            chunk_overlap=100
        )
        self.create_pinecone_index(self.vectorstore_index_name)
        self.vectorstore = PineconeVectorStore(
            index_name=self.vectorstore_index_name,
            embedding=self.embeddings,
            pinecone_api_key=os.getenv("PINECONE_API_KEY")
        )
        self.rag_prompt = hub.pull(
            "rlm/rag-prompt", 
            api_key=os.getenv("LANGSMITH_API_KEY")
        )
        config = RailsConfig.from_path("./config")

        self.guardrails = RunnableRails(config=config,llm=self.groq_llm)


    def create_pinecone_index(self, vectorstore_index_name):
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))  
        spec = ServerlessSpec(cloud='aws', region='us-east-1')  
        if vectorstore_index_name in pc.list_indexes().names():  
            pc.delete_index(vectorstore_index_name)  
        pc.create_index(  
            vectorstore_index_name,  
            dimension=1536,
            metric='dotproduct',  
            spec=spec  
        )  
        while not pc.describe_index(vectorstore_index_name).status['ready']:  
            time.sleep(1) 

    def load_docs_into_vectorstore_chain(self):
        docs = self.loader.load()
        split_docs = self.text_splitter.split_documents(docs)
        self.vectorstore.add_documents(split_docs)

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    def create_retrieval_chain(self):
        self.load_docs_into_vectorstore_chain()
        self.retriever = self.vectorstore.as_retriever()
        self.rag_chain = (
                        {
                            "context": self.retriever | self.format_docs, "question": RunnablePassthrough()
                        }
                        | self.rag_prompt
                        | self.groq_llm
                        | StrOutputParser()
                    )
        self.rag_chain = self.guardrails | self.rag_chain
    def qa(self, query, vectorstore_created):
        if vectorstore_created:
            pass
        else:
            self.create_retrieval_chain()
        return self.rag_chain.invoke(query), True

# if __name__=="__main__":
#     rag = RAG("https://lilianweng.github.io/posts/2023-06-23-agent/")
#     print(rag.qa("What are the components in an agent system", False))
    
