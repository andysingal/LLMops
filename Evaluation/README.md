[Self-improving evaluation in LangSmith](https://blog.langchain.dev/aligning-llm-as-a-judge-with-human-preferences/)

[Custom-Metrics](https://github.com/rajib76/ragas_examples/blob/main/custom_metrics/criminality.py)

[Custom LLM Evaluations ⚙️: Function Calling Agent](https://www.youtube.com/watch?v=EfhylWtNb1s)

[SummHay benchmark](https://github.com/salesforce/summary-of-a-haystack)

[Deepval-LlamaIndex](https://docs.confident-ai.com/docs/integrations-llamaindex) 


[DocBench](https://github.com/Anni-Zou/DocBench) 

[ragas_examples](https://github.com/rajib76/ragas_examples/blob/main/05_answer_correctness.py)

[langsmith-evaluation-helper](https://github.com/gaudiy/langsmith-evaluation-helper)


[LLM Hallucination Index](https://github.com/rungalileo/hallucination-index) 

[langfuse-RAGAS](https://langfuse.com/guides/videos/beginners-guide-to-rag-evaluation)



[Running SWE-bench with LangSmith](https://docs.smith.langchain.com/tutorials/Developers/swe-benchmark)

[arena-hard-auto](https://github.com/lmarena/arena-hard-auto)

[WebCode: Search Evals for Coding Agents](https://exa.ai/blog/webcode)




### Article

[How to use prebuilt evaluators](https://docs.smith.langchain.com/evaluation/how_to_guides/prebuilt_evaluators)

[Evaluating Accuracy in RAG Applications: A Guide to Automated Evaluation](https://dzone.com/articles/rag-accuracy-metrics-automated-evaluation)

[Evaluating Long-Context Question & Answer Systems](https://eugeneyan.com/writing/qa-evals/?twclid=2-44mq6dobl8i4tvgb8wcu9shwd)

[Mastering LLM Quality: A Key Guide for DeepEval & Red Teaming](https://blog.nashtechglobal.com/mastering-llm-quality-a-key-guide-for-deepeval-red-teaming/)

[The Best Platforms for Evaluating AI Models in 2025](https://dev.to/debmckinney/the-best-platforms-for-evaluating-ai-models-in-2025-25ed)

[Using Autoresearch to improve harness skills](https://x.com/alokbishoyi97/status/2059610305408462898)

You give it a codebase, a definition of "better", and a budget. It sets up a benchmark (or uses one you already have), generates hypotheses about what to change, runs each hypothesis in its own isolated workspace, scores the result, and keeps a tree of attempts.

Three things make evo different from a single greedy hill-climb thats typical in autoresearch implementations :
- parallel exploration - Multiple agents run at the same time, each in its own sandbox, each trying a different hypothesis. They don't have to wait their turn.
- tree search, not linear - evo doesn't only keep the single highest-scoring branch. It keeps branches that win on different slices of the task - specialists alongside generalists. When those specialists can be merged, the result is usually better than either parent alone.
- gates - any pass/fail check you can write (a regression test, a held-out slice, a no-cheating audit) is a gate. An experiment that fails a gate gets discarded even if its score is the best so far. Without gates, optimization loops find ways to game the metric.

```
/evo:discover : is the one-time setup. You point it at a codebase and tell it what you want better. It explores the repo, figures out a benchmark (or instruments one if none exists), proposes the optimization target, and registers any gates that should run on every experiment.
```



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

<img width="444" height="394" alt="Screenshot 2025-08-04 at 2 53 21 PM" src="https://github.com/user-attachments/assets/5c419b43-6f41-4aac-9fb8-8594e94d5e12" />


### Resources

[Notebooks](https://github.com/mingyin0312/RLFromScratch/tree/main)


<img width="732" height="335" alt="Screenshot 2025-10-24 at 2 44 59 PM" src="https://github.com/user-attachments/assets/6221dfa8-9ad0-4ecb-980e-5548c5c0a55a" />


### Article

[Jev-as-a-Judge for Agent Evals](https://www.langchain.com/blog/jev-agent-evals-langsmith)

<img width="741" height="567" alt="Screenshot 2026-09-20 at 2 16 49 PM" src="https://github.com/user-attachments/assets/42758378-e25c-4831-8fb4-d89ffa060d24" />

Jev supports three types of questions:

Choice selects one option and returns probabilities and confidence
- Example: “Is the final answer grounded in the retrieved evidence?”
- Response: A float from 0.0 to 1.0, where 1.0 means fully grounded
-‍ Score rates an answer against an ordered rubric and returns probabilities and confidence‍

‍Example: “How useful is the answer?”
Response: A rubric score from 1 (unhelpful) to 5 (highly useful), plus probabilities and confidence
- Noul returns the probability that a yes/no judgment is true
- Example: “Which search outcome best describes this run?”
- Response: One of searched_appropriately, searched_unnecessarily, or failed_to_search, plus probabilities and confidence

- Jev does not generate an explanation and then convert that text into a score. It returns typed answers and probabilities directly. 

<img width="720" height="337" alt="Screenshot 2026-09-20 at 2 19 30 PM" src="https://github.com/user-attachments/assets/0b6c9a2e-a81b-40b3-bc0c-ad9229cc5eb1" />


<img width="764" height="369" alt="Screenshot 2026-09-20 at 2 13 26 PM" src="https://github.com/user-attachments/assets/946bbcb7-9749-4a8f-b2b5-35b4e26d8adc" />


