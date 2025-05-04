[Self-improving evaluation in LangSmith](https://blog.langchain.dev/aligning-llm-as-a-judge-with-human-preferences/)

[Custom-Metrics](https://github.com/rajib76/ragas_examples/blob/main/custom_metrics/criminality.py)

[Custom LLM Evaluations ⚙️: Function Calling Agent](https://www.youtube.com/watch?v=EfhylWtNb1s)

[SummHay benchmark](https://github.com/salesforce/summary-of-a-haystack)

[Deepval-LlamaIndex](https://docs.confident-ai.com/docs/integrations-llamaindex) 


[DocBench](https://github.com/Anni-Zou/DocBench) 

[ragas_examples](https://github.com/rajib76/ragas_examples/blob/main/05_answer_correctness.py)

[langsmith-evaluation-helper](https://github.com/gaudiy/langsmith-evaluation-helper)


[LLM Hallucination Index](https://github.com/rungalileo/hallucination-index) 



[Running SWE-bench with LangSmith](https://docs.smith.langchain.com/tutorials/Developers/swe-benchmark)

[arena-hard-auto](https://github.com/lmarena/arena-hard-auto)


### Article

[How to use prebuilt evaluators](https://docs.smith.langchain.com/evaluation/how_to_guides/prebuilt_evaluators)


<img width="585" alt="Screenshot 2024-08-22 at 10 30 29 PM" src="https://github.com/user-attachments/assets/15bb43e0-3474-434b-a858-cf5cbbd110d6">

```py
import asyncio
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import Faithfulness
from ragas.llms import LangchainLLMWrapper
from langchain_groq import ChatGroq

llm = ChatGroq( model="deepseek-r1-distill-llama-70b", temperature=0.0,max_retries=2)
evaluator_llm = LangchainLLMWrapper(llm)

sample = SingleTurnSample(
    user_input="When was the first super bowl?",
    response="The first superbowl was held on Jan 15, 1967",
    retrieved_contexts=[
        "The First AFL–NFL World Championship Game was an American football game played on January 15, 1967, at the Los Angeles Memorial Coliseum in Los Angeles."
    ]
)

scorer = Faithfulness(llm=evaluator_llm)

async def main():
    score = await scorer.single_turn_ascore(sample)
    print(score)

asyncio.run(main())
```
