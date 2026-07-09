vLLM is an open-source inference engine built around PagedAttention and continuous batching. It manages the KV cache in non-contiguous memory blocks (the way an OS manages virtual memory pages), which eliminates the memory fragmentation that plagued earlier serving stacks, and it ships an OpenAI-compatible API out of the box. The practical upshot: pip install vllm, point it at a Hugging Face model ID, and you have a production-grade endpoint in minutes.

#### [PagedAttention: virtual memory for KV caches](https://www.runpod.io/articles/guides/vllm-pagedattention-continuous-batching)

PagedAttention is a smart memory-saving technique for AI. Instead of reserving huge, rigid chunks of GPU memory for conversations, it breaks a conversation’s memory into small, flexible "pages". These can be stored anywhere and stitched together using an index map, preventing massive amounts of wasted space

Under the hood, vLLM ships a custom CUDA kernel that gathers non-contiguous blocks via the block table at each attention step, selecting from FlashAttention-2 or FlashAttention-3 based on GPU capabilities.

### Prefix caching

vLLM’s prefix caching stores KV blocks for shared prompt prefixes (system prompts, chat templates, few-shot examples) across requests. When two requests share the first 512 tokens of a system prompt, vLLM re-uses the pre-computed KV blocks for those tokens rather than recomputing them


### Chunked prefill
 With chunked prefill enabled via --enable-chunked-prefill (on by default in vLLM V1), vLLM splits long prefills into configurable chunks and interleaves them with decode operations. The default chunk budget is 2048 tokens in recent releases (v0.8.x+), up from the earlier 512-token default. Decode requests for short sequences proceed in parallel with chunks of the long prefill, keeping p50 latency stable even when long-context requests arrive.(Note: Chunked prefill is a vLLM feature that breaks large, time-consuming user prompts into smaller chunks, allowing the AI to process them across multiple steps. Instead of completely pausing other ongoing text generations to read a massive prompt all at once, vLLM works on the prompt a little at a time while interleaving responses)


 ### Speculative decoding

 Per-token decode latency can be cut further with speculative decoding, which pairs a small draft model with the target model. The draft model generates N candidate tokens in a single forward pass, and the target model verifies all N tokens simultaneously. When the draft model’s predictions align with the target model’s distribution, you get N tokens out of one target model forward pass. When a draft token is rejected, the target model discards all subsequent draft tokens and samples a correction token from its own distribution

 Acceptance rate is workload-dependent. Code completion and templated outputs with low entropy often achieve 70-90% acceptance; open-ended creative generation can fall to 20-40%. At low acceptance rates, the extra draft model forward pass adds overhead without reducing target model forward pass count, and net throughput can regress. vLLM exposes vllm:spec_decode_draft_acceptance_rate in its Prometheus metrics for empirical tuning, and enables the feature with --speculative-model and --num-speculative-tokens.


### Quantization
- vLLM supports AWQ, GPTQ, FP8, and INT8 weight quantization. KV cache quantization is currently available for FP8 only (INT8 KV cache quantization is a pending feature request, not yet supported). The choice between formats depends on your hardware and quality tolerance
- AWQ and GPTQ compress weights to 4-bit precision, cutting VRAM requirements by roughly 4x at the cost of a calibration step and a small quality regression that varies by model; AWQ is the more commonly used of the two for vLLM deployments





[How to run gpt-oss with vLLM](https://cookbook.openai.com/articles/gpt-oss/run-vllm)

[Batch inference on OpenShift AI with Ray Data, vLLM, and CodeFlare](https://developers.redhat.com/articles/2025/08/07/batch-inference-openshift-ai-ray-data-vllm-and-codeflare#)

[Ollama to vLLM a Roadmap for Scalable LLM Deployment](https://blog.gopenai.com/ollama-to-vllm-a-roadmap-for-scalable-llm-deployment-337775441743)


[SGLang vs vLLM: A Technical Comparison for Self-Hosted Deployments](https://x.com/Mayhem4Markets/article/2069090022117019928)

- Both engines support an extensive and overlapping set of quantization formats as of mid-2026. vLLM supports FP8, MXFP8/MXFP4, NVFP4, INT8, INT4, GPTQ/AWQ, GGUF, compressed-tensors, ModelOpt, TorchAO, AutoAWQ, BitsAndBytes, GPTQModel, Intel Neural Compressor, LLM Compressor, and AMD Quark
- SGLang supports fp8, mxfp4, blockwise_int8, w8a8_int8, w8a8_fp8, awq, gptq, compressed-tensors, gguf, modelopt_fp8, modelopt_fp4, torchao, bitsandbytes, awq_marlin, gptq_marlin, and AMD-specific methods including quark_int4fp8_moe, quark_mxfp4, and petit_nvfp4
- On memory efficiency, the architectural difference between PagedAttention and RadixAttention targets different sources of waste. PagedAttention eliminates wasted GPU memory from padded sequences and early-finishing requests, allowing vLLM to serve more concurrent users on the same GPU than a naive implementation. RadixAttention reduces the effective per-request memory footprint when prompts share context, which benefits chatbot, RAG, and agentic workloads where system prompts and conversation history are reused across turns.
- vLLM has more mature Docker tooling with official images, Helm charts for Kubernetes, and extensive production deployment documentation. SGLang supports Docker deployment and can be deployed on Kubernetes, but the guides are less comprehensive. For a setup running behind a reverse proxy on a single machine, both engines work equally well with Docker Compose.
- Both frameworks support speculative decoding, the technique of using a smaller draft model to predict tokens that a larger target model then verifies in parallel. vLLM supports n-gram, suffix, EAGLE, and DFlash speculative decoding. SGLang supports DFlash and Spec V2, with the latter introduced in June 2026 as the next generation of speculative decoding.



#### Examples
[Example_1](https://github.com/vishakhasadhwani/llm-deployment-demo/blob/main/g4-instance-setup.md)

[Native-speed vLLM transformers modeling backend](https://huggingface.co/blog/native-speed-vllm-transformers-backend)

