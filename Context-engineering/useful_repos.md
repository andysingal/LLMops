[breathe-memory](https://github.com/tkenaz/breathe-memory)

LLMs forget. Context windows are finite and expensive. Most solutions either stuff everything in (burns tokens) or summarize (loses structure).

BREATHE does neither:

- SYNAPSE (inhale) — before each generation, extracts associative anchors from the user message and injects semantically relevant memories directly into the prompt. The LLM starts thinking with context already loaded. Overhead: 2–20ms.

- GraphCompactor (exhale) — when context fills up, extracts a structured graph (topics, decisions, open questions, artifacts) instead of a lossy narrative summary. Typically saves 60–80% of tokens while preserving semantic structure.

```
import asyncio
from breathe import Synapse, GraphCompactor, BreatheConfig
from breathe.interfaces import MemoryRepository, LLMClient, RetrievedNode

# Implement these two interfaces for your backend
class MyMemoryRepo(MemoryRepository):
    async def get_concepts(self):
        return {"FastAPI": "uuid-001", "Redis": "uuid-002"}

    async def graph_bfs(self, start_ids, **kwargs):
        return []  # implement BFS against your DB

    async def keyword_search(self, keywords, limit=5):
        return []  # implement ILIKE against your memories table

class MyLLMClient(LLMClient):
    async def complete(self, prompt, max_tokens=4000, temperature=0.2):
        # call your LLM API here
        ...

async def main():
    config = BreatheConfig()
    synapse = Synapse(repository=MyMemoryRepo(), config=config)
    await synapse.initialize()

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "How should I structure my FastAPI endpoints?"},
    ]

    # Inject associative memory before each LLM call
    messages = await synapse.inject(messages)

    # When context gets full, compress with GraphCompactor
    compactor = GraphCompactor(llm_client=MyLLMClient())
    result = await compactor.compress(messages)
    messages = result["compressed_messages"]

asyncio.run(main())
```
