[Sift](https://github.com/shreyaskarnik/Sift)

Sift through the noise. Score your feed with EmbeddingGemma, right in the browser.

Inspired by google/embeddinggemma-tuning-lab

Sift is a Chrome extension that runs EmbeddingGemma directly in the browser via Transformers.js + WebGPU:

EmbeddingGemma-300M (q4) — scores content against your interests using cosine similarity
Current site support (for now): Hacker News, Reddit, and X. More site integrations are planned. On supported sites, Sift dims low-relevance items so the good stuff stands out.

Users can label items (thumbs up/down) to collect training data, export it as CSV, and fine-tune the model with the included Python pipeline.
