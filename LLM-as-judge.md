[LLM-as-a-Judge for AI Systems](https://muditb.com/llm-as-a-judge-for-ai-systems/)

[Mixture-of-Judges](https://x.com/_philschmid/status/1841752199904317868/photo/1)

[Artificial Intelligence LLM-as-a-Judge: A Scalable Solution for Evaluating Language Models Using Language Models](https://www.unite.ai/llm-as-a-judge-a-scalable-solution-for-evaluating-language-models-using-language-models/)

[RAG Evaluation with LLM-as-a-Judge + Synthetic Dataset Creation](https://generativeai.pub/rag-evaluation-with-llm-as-a-judge-synthetic-dataset-creation-7fce566310f5)

[Improve factual consistency with LLM Debates](https://aws.amazon.com/blogs/machine-learning/improve-factual-consistency-with-llm-debates/)

[Llama-Bench](https://github.com/ggerganov/llama.cpp/blob/master/examples/llama-bench/README.md)

[Arize-judge](https://github.com/Arize-ai/phoenix/blob/main/tutorials/evals/optimizing_llm_as_a_judge_prompts.ipynb)


[langchain-llm-judge](https://github.com/langchain-ai/claude-code-evals/blob/main/task_3/llm_as_a_judge.py)

<img width="1166" alt="Screenshot 2024-11-30 at 6 51 32 PM" src="https://github.com/user-attachments/assets/02a1087a-da9c-4efa-a0b2-3894611b7806">


![Screenshot 2024-11-29 084421](https://github.com/user-attachments/assets/b4b46cc5-c2f6-4928-8e47-30e455c79cf2)


    Aspect	            Task	                                  Definition

1. Semantic Coverage  Text summarization             How many semantic content units from the reference text are covered by the generated text?

2. Factuality  Text summarization             Does the generated text preserve the factual statements of the source text?

3. Consistency  Text summarization, Dialogue response generation       Is the generated text consistent in the information it provides?

4. Informativeness  Text summarization, Data to text, Dialogue response generation       How well does the generated text capture the key ideas of its source text?

5. Coherence   Text summarization, Dialogue response generation              How much does the generated text make sense?

6. Relevance   Dialogue response generation, Text summarization, Data to text            How well is the generated text relevant to its source text?

7. Fluency  Dialogue response generation, Text summarization, Data to text, Machine translation    Is the generated text well-written and grammatical?

8. Accuracy  Machine translation  Are there inaccuracies, missing, or unfactual content in the generated text?

9. Interest  Dialogue response generation  Is the generated text interesting?

10. Engagement Dialogue response generation Is the generated text engaging?

11. Specific Dialogue response generation  Is the generated text generic or specific to the source text?

12. Correctness Dialogue response generation  Is the generated text correct or was there a misunderstanding of the source text?

13. Semantically appropriate  Dialogue response generation  Is the generated text semantically appropriate?

14. Understandability  Dialogue response generation  Is the generated text understandable?

15. Error Recovery  Dialogue response generation  Is the system able to recover from errors?

16. Diversity  Dialogue response generation  Is there diversity in the system responses?

17. Depth  Dialogue response generation  Does the system discuss topics in depth?

18. Likeability  Dialogue response generation  Does the system display a likable personality?

19. Flexibility Dialogue response generation  Is the system flexible and adaptable to the user and their interests?

20. Inquisitiveness   Dialogue response generation  Is the system inquisitive throughout the conversation?



<img width="654" alt="Screenshot 2024-10-05 at 10 06 35 AM" src="https://github.com/user-attachments/assets/a981ea5c-4f3d-4d14-9f0d-b666b633c713">




How can we mitigate reward hacking in RLHF? 🤔 Constrained Generative Policy Optimization (CGPO) is a new RLHF method using Mixture of Judges (MoJ) from 
@AIatMeta
. CGPO outperforms PPO (single RM) on Alpaca Eval, Arena Hard, IFEval! 👀

Implementation
- 1️⃣ Select pre-trained LLM (e.g., Llama 3.0 70B) and SFT the model using datasets for various tasks (general chat, math, instruction following).
- 2️⃣ Create Mixture of Judges (MoJ) - combine rule-based and LLM-based judges for constraint evaluation (optionally train different RM, e.g. helpfulness)
- 3️⃣ Implement warm-up phase using DPO for a few steps on combined reward data.
- 4️⃣ Use CGPO: Sample prompts, generate responses, apply MoJ for constraint evaluation, and update the policy using a constrained optimizer (CRPG, CODPO, or CRRAFT).

Insights
- 💡 MoJ prevents reward hacking and boosts performance by enforcing constraints.
- 📈 Outperforms PPO and DPO in benchmarks like AlpacaEval (+7.4%), Arena-Hard (+12.5%), and others.
- 🧮  2-5% gains in math, coding, and knowledge tasks
- 🔄 Warm-up phase with DPO significantly boosts final performance
- ⚙️ Allows tailoring of reward models, judges, and optimizer settings for individual tasks.
- ❌ Requires significantly more computing as their are multiple reward models/judges

![Screenshot 2024-10-03 084414](https://github.com/user-attachments/assets/1e2fcb88-6a01-4943-963f-09611046e2b0)
