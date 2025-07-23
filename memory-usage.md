[How to Reduce Memory Use in Reasoning Models](https://huggingface.co/blog/Kseniase/lightthinker-mla)

[cognee](https://github.com/topoteretes/cognee)

- vLLM comes with a good approach, a feature called PagedAttention that manages the KV cache dynamically, like a paging system in an OS, to eliminate fragmentation and enable continuous token generation across multiple requests without memory waste
- SGLang with RadixAttention
SGLang is a model-serving framework that focuses on optimizing the KV cache across multiple LLM requests. Since KV cache computation depends on prefix tokens, requests with the same prompt prefix can reuse the KV cache, reducing redundant computation and memory usage.

In existing inference engines, the KV cache for a request is discarded after its own generation is completed and is not reused across multiple calls. If the input prompts of the requests happen to have many common prefixes, recomputing all the KV cache is not efficient and reusing them can vastly reduce the serving latency. So SGLang came up with a feature called RadixAttention, which maintains a LRU cache of the KV cache for all requests within a radix tree; it enables automatic reuse of the KV cache across multiple generation calls efficiently.

