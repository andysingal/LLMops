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
