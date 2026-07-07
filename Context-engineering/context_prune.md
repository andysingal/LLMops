[Building a Context Pruning Pipeline for Long-Running Agents](https://machinelearningmastery.com/building-a-context-pruning-pipeline-for-long-running-agents/)

- Why unbounded conversation history is a problem for agents built on top of large language models, and what a context pruning strategy looks like.
- How to use sentence transformer embedding models to compute semantic similarity between a current prompt and archived conversation turns.
- How to assemble a pruned context window from the most recent turn, the top-K semantically relevant past turns, and the current prompt.

[How we taught a small LLM to throw away 68% of our RAG context](https://www.kapa.ai/blog/how-we-prune-rag-context)

