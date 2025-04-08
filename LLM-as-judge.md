[LLM-as-a-Judge for AI Systems](https://muditb.com/llm-as-a-judge-for-ai-systems/)

[Mixture-of-Judges](https://x.com/_philschmid/status/1841752199904317868/photo/1)

[Artificial Intelligence LLM-as-a-Judge: A Scalable Solution for Evaluating Language Models Using Language Models](https://www.unite.ai/llm-as-a-judge-a-scalable-solution-for-evaluating-language-models-using-language-models/)

[RAG Evaluation with LLM-as-a-Judge + Synthetic Dataset Creation](https://generativeai.pub/rag-evaluation-with-llm-as-a-judge-synthetic-dataset-creation-7fce566310f5)

[Improve factual consistency with LLM Debates](https://aws.amazon.com/blogs/machine-learning/improve-factual-consistency-with-llm-debates/)

[Llama-Bench](https://github.com/ggerganov/llama.cpp/blob/master/examples/llama-bench/README.md)

[Arize-judge](https://github.com/Arize-ai/phoenix/blob/main/tutorials/evals/optimizing_llm_as_a_judge_prompts.ipynb)

<img width="1166" alt="Screenshot 2024-11-30 at 6 51 32 PM" src="https://github.com/user-attachments/assets/02a1087a-da9c-4efa-a0b2-3894611b7806">


![Screenshot 2024-11-29 084421](https://github.com/user-attachments/assets/b4b46cc5-c2f6-4928-8e47-30e455c79cf2)



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
