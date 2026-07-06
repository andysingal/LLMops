[ZeroGPU-llm](https://zhuanlan.zhihu.com/p/1948508558908958339)

[GPU Memory Math for LLMs](https://x.com/TheAhmadOsman/status/2040103488714068245)

These tools serve different purposes / occupy different layers
- Local portability
- Consumer CUDA
- Apple unified-memory workflows
- Quantized inference
- Production serving
- Distributed orchestration
- Vendor-optimized datacenter execution

### one-page decision guide
- Laptop / edge / odd hardware → llama.cpp
- Mac-first workflows → MLX / MLX-LM
- Single RTX local inference → ExLlamaV2
- 2-4+ NVIDIA / CUDA GPUs → ExLlamaV3
- General production serving → vLLM
- Long-context / MoE / routing → SGLang
- NVIDIA max performance → TensorRT-LLM
- Cluster orchestration → NVIDIA Dynamo

