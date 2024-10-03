[LLM-as-a-Judge for AI Systems](https://muditb.com/llm-as-a-judge-for-ai-systems/)

[Mixture-of-Judges](https://x.com/_philschmid/status/1841752199904317868/photo/1)

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
