[How to Reduce Memory Use in Reasoning Models](https://huggingface.co/blog/Kseniase/lightthinker-mla)

[cognee](https://github.com/topoteretes/cognee)

- vLLM comes with a good approach, a feature called PagedAttention that manages the KV cache dynamically, like a paging system in an OS, to eliminate fragmentation and enable continuous token generation across multiple requests without memory waste
- SGLang with RadixAttention
SGLang is a model-serving framework that focuses on optimizing the KV cache across multiple LLM requests. Since KV cache computation depends on prefix tokens, requests with the same prompt prefix can reuse the KV cache, reducing redundant computation and memory usage.

In existing inference engines, the KV cache for a request is discarded after its own generation is completed and is not reused across multiple calls. If the input prompts of the requests happen to have many common prefixes, recomputing all the KV cache is not efficient and reusing them can vastly reduce the serving latency. So SGLang came up with a feature called RadixAttention, which maintains a LRU cache of the KV cache for all requests within a radix tree; it enables automatic reuse of the KV cache across multiple generation calls efficiently.

[Understanding Episodic Memory in Artificial Intelligence](https://www.digitalocean.com/community/tutorials/episodic-memory-in-ai)

Episodic memory enables artificial agents to remember and retrieve specific events from their past experiences, making them more context-aware and better able to learn from their own history. It provides detailed contextual information, while semantic memory maintains general facts.


***** AI Agent session : everything inside the box is ephemeral 

User Prompt --------------
                          |

Current Chat History ----- >   Working memory/ Context RAM  ---> LLLM - Q & A Agent (GPT, Claude) ---> Reply
                          |
System Prompt ------------


Working memory/ context RAM

(skill.md)
1. Procedural Memory(Files, Text)                        (RAG(top-k search))
                                                          2. Semantic Memory(Vector Store)
                                                          - durable facts
                                                          - user profile
- How to act(how the agent should act)
- skills Instructions



3. Episodic Memory(Vector store)----> RAG(top-k search)    --- saves the messages/activities
- dated events
- past chat history

#### Article

[Your KV Caching Is Broken](https://x.com/akshay_pachaar/status/2074502882812952666)

But prefix caching has a hard ceiling.
The cached portion must be an exact, byte-for-byte prefix of the new request. Change anything in the cached region (even a single character) and you get a full cache miss.
This breaks in three common scenarios:

- RAG with multiple documents: You cached document A alone and document B alone. A new query needs both. The second document's cached KV state is invalid because it was computed without awareness of the first document.
- Document order changes: The same three documents appear in different orders across requests. Every permutation is a cache miss, even though the documents themselves are identical.
- Growing conversation history: Each new turn changes the full context after the prefix. Earlier cached states beyond the stable prefix become useless.

Google's TurboQuant, a recent KV cache quantization technique, compresses the cache to 3 bits per value with zero accuracy loss. But when it runs inside the inference engine, it causes 20%+ inference slowdown.

Cache management and inference serving are fundamentally different workloads. One is I/O-heavy (moving large tensors between GPU, CPU, and storage). The other is compute-heavy (matrix multiplications on GPU).
Forcing both into the same process is like running a database and a web server in the same thread. It works until load hits, and then everything fights for the same resources.

***LMCache and the disaggregated approach
LMCache is an open-source project that takes a fundamentally different approach. Instead of running cache management inside the inference engine, it runs as a completely separate process alongside it.


This separation produces three concrete wins.
- No resource contention: Cache I/O never blocks inference, and inference never blocks cache I/O. The 20% throughput loss from running optimization techniques inside the engine disappears.
- Zero-copy sharing across GPUs: In the traditional setup, sharing cached data between two GPUs requires multiple memory copies. LMCache lets both GPUs read and write the same memory region directly, skipping those copies entirely.
- Multi-tier parallel loading: Cached data can live across GPU memory, CPU RAM, local SSD, and remote storage. Traditional approaches check these one by one, bottlenecking on the slowest tier. LMCache checks all of them simultaneously and streams data from wherever it finds a match, in parallel.

LMCache delivers 14x faster time-to-first-token and 4x faster decoding compared to in-process caching. Startup time drops from over 3 minutes to about 30 seconds.

##### Solving the prefix problem with CacheBlend

CacheBlend exploits this by identifying just those few tokens and selectively recomputing only them. Everything else gets reused as-is from the independent caches.

For teams building RAG systems, multi-document Q&A, or agents that accumulate context from multiple sources, this turns every document in the knowledge base into a reusable cached asset, regardless of what order it appears in or what other documents sit alongside it.

LMCache isn't a research prototype. It ships with the infrastructure that production teams expect.
- Prometheus and OpenTelemetry integration for tracking cache hit rates and I/O performance.
- Kubernetes operator for deployment
- CLI for debugging and benchmarking.
The fault tolerance design is worth noting.


