[agentic-rag-financial-parser](https://github.com/Ambuj123-lab/agentic-rag-financial-parser)

I ditched the expensive LLM parser, switched to raw PyMuPDF, and built a highly specialized ingestion pipeline:

- Custom Regex Parsing — Split the page text directly at the ______ footnote line. Discarded the bottom half. 0 footnotes ingested.

- Article-Level Chunking — Scrapped RecursiveCharacterTextSplitter for the parent chunks. Split the document purely on Article regex boundaries. This gave me 3,248 precise parent/child chunks.

- Metadata Injection — Extracted the Article number via regex and hardcoded it into the chunk's metadata before uploading to Pinecone ({"article_number": "19"}).

- Smart Routing — My [LangGraph router](https://www.reddit.com/r/Rag/comments/1vgblto/when_a_generalpurpose_llm_parser_wasnt_enough_how/) detects if the query is asking for a specific Article. If yes, it passes article_number to the retriever. The retriever applies a strict Pinecone metadata filter ({"article_number": {"$eq": "19"}}) and bypasses normal vector search entirely.
