LLM Inference Engineering: Quantization - The Complete Introduction

1.  It is the process of reducing the precision of the parameters of a model to make it smaller and less memory-intensive. The goal is to do this while preserving accuracy.
    
2.  If done right, it can improve latency metrics (TTFT/TPS), throughput, etc. But when it is done wrong, it can have a huge impact on output quality.
    
3.  Models have weights, activations, representations, etc. Most of the time, they are stored in FP16, BF16, etc.
    
4.  Reducing precision by half improves both phases of inference:
-   Prefill: Compute-bound, runs on lower-precision tensor cores with twice the FLOPS.
-   Decode: Memory-bound, loads half as much data per value, doubling the bandwidth.
    
5.  It is not all linear improvement; you cannot expect twice as fast in practice. Most of the time, it is 30–50% better performance for LLMs.
    
6.  The biggest problem is that it has the risk of reducing the model's output quality. It can introduce precision errors, which can compound drastically. Much of the work in this domain is about preventing/minimizing the impact on the final model output.
    
7.  FP64, the highest precision, is only used for high-precision scientific computing, not much in AI training/inference, which leaves 16-, 8-, and 4-bit for our use case.
    
8.  Each format has a Scale Factor: a multiplier used to map low-precision values back to high-precision ones. Dynamic Range: the difference between the lowest and highest value that can be represented using that format. Granularity: the number of parameters that are quantized along a single scale factor.
    
9.  FP formats have a Sign, Exponent, and Mantissa. An FP8 number may contain a 4-bit exponent, 3-bit mantissa, and 1 bit for the sign.
    
10.  There are different levels at which quantization can be applied.
-   Tensor level: a single scale factor for the entire QKV tensor.
-   Channel level: a different scale factor for each feature vector within a tensor.
-   Block level: within each feature vector, divide it into blocks of N values and calculate the scale factor for each block.
   
11.  GGUF is the most popular choice for distributing highly quantized models on Hugging Face.
    
12.  Quantization handles quality loss through dynamic quantization, which means that certain layers are left in their original precision, while others are quantized to integers (or something of much lower precision if not INT).
    
13.  The more parameters a model has, the less sensitive it is to quantization.
    
14.  Quantization-aware training: training weights and computing scale factors together.
    
15.  Post-training quantization: converting final model weights to a new precision by computing scale factors.
    
16.  There are two decisions one needs to make: 1. What parts of the model (weights, activations, KV cache, attention) should be quantized? 2. What number format will work for the problem? It is a tradeoff.
    
17.  Weights > activations > KV Cache > Attention. From least to most sensitive to quantization.

(end)  

This is the collection of notes made while reading Inference Engineering Book by Philip Kiely. More posts will be there soo
