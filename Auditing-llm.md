


## Articles
[When AI Snitches: Auditing Agents That Spill Your Model’s (Alignment) Tea](https://www.getmaxim.ai/blog/when-ai-snitches-auditing-agents-that-spill-your-models-alignment-tea/)

[llm-audit](https://github.com/Javierlozo/llm-audit)

```
# 1. Install the engine (one-time, system-wide).
brew install semgrep        # or: pipx install semgrep

# 2. Sanity-check setup. Lists missing dependencies and how to fix them.
npx llm-audit doctor

# 3. See what the rules catch in 5 seconds. No setup in your repo.
npx llm-audit demo

# 4. Run on your own code.
npx llm-audit scan
```
