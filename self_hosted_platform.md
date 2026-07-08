[CloudShipai](https://github.com/cloudshipai/station)

Build multi-agent systems that coordinate like real teams. Test with realistic scenarios. Deploy on your infrastructure.

Station gives you:

- ✅ Multi-Agent Teams - Coordinate specialist agents under orchestrators
- ✅ Built-in Evaluation - LLM-as-judge tests every agent automatically
- ✅ Git-Backed Workflow - Version control agents like code
- ✅ One-Command Deploy - Push to production with stn deploy
- ✅ Full Observability - Jaeger traces for every execution
- ✅ Self-Hosted - Your data, your infrastructure, your control

[How to Self-Host Your AI Stack Without OpenAI](https://www.ayautomate.com/blog/self-host-ai-stack-without-openai)

[I tried using Langfuse as a self-host with DGX Spark to observe and evaluate an LLM application](https://dev.classmethod.jp/articles/langfuse-self-host-llm-observability-handson/)

<img width="737" height="542" alt="Screenshot 2026-05-02 at 8 12 13 AM" src="https://github.com/user-attachments/assets/637c6897-ebfc-47f1-9225-b59dd882fbff" />

[docker-ai-stack](https://github.com/hwdsl2/docker-ai-stack)

Deploy a complete, self-hosted AI stack on your own server with a single command.

- Zero-config: all services auto-configure on first start
- Secure: Ollama, LiteLLM, and MCP Gateway generate API keys automatically
- Private: audio, embeddings, and LLM inference all run locally — no data sent to third parties
- Optional auth: Whisper, Kokoro, and Embeddings work without API keys by default (set keys via env files for public deployments)
- Lightweight stacks for lower memory requirements (as low as ~2.5 GB)
- GPU acceleration via NVIDIA CUDA

[shannon](https://github.com/KeygraphHQ/shannon)

Shannon is an autonomous, white-box AI pentester for web applications and APIs.
It analyzes your source code, identifies attack vectors, and executes real exploits to prove vulnerabilities before they reach production.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[How Lyft Built a Self-Serve AI Agent Platform for Customer Support with LangGraph and LangSmith](https://www.langchain.com/blog/lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith)

Our "self-serve" platform integrates LangGraph’s subgraph architecture with LangSmith’s robust tracing and monitoring tools, empowering non-technical domain experts to develop and refine AI agents independently. This shift has accelerated agent development from roughly six months to just a few weeks, all while upholding high standards through an automated LLM-as-a-judge evaluation system.

This led us to a pivotal question: Could we empower ops teams, VoC leads, and product managers to construct and refine agents directly using natural language? Our goal was to eliminate the technical intermediary from the daily iteration process to accelerate learning and deployment. 


[llmaker](https://github.com/raiyanyahya/llmaker)

```
# ── Build a complete application stack ──────────────────────────
llmaker stack up assistant      # one command → a private ChatGPT-style UI over a local model
llmaker stack init rag          # …or scaffold any stack to edit, then apply it:
llmaker apply                   #   assistant · voice · rag · research · code · chatbot · faq · recommend · sql

# ── …or run a single model (OpenAI-compatible) ──────────────────
llmaker up --model llama3:8b    # a local endpoint — explicit, or a preset:
llmaker up chat                 #   chat · code · small · embed · vision
llmaker chat <name>             # test it in the terminal
llmaker open <name>             # open its built-in web UI

# ── …or compose the stack à la carte, service by service ────────
llmaker service catalog         # browse what's available
llmaker service add qdrant      # vector database  → qdrant:6333
llmaker service add redis       # cache / memory   → redis:6379
llmaker service add langfuse    # observability    → langfuse:3000

# ── Operate the fleet ───────────────────────────────────────────
llmaker ls                      # every model + service, one view   (--json)
llmaker top                     # live resource dashboard (TUI)
llmaker status <name>           # gauges, loaded models, endpoints
llmaker logs <name> -f          # stream logs from any container
llmaker pull mistral --on chat  # download a model with progress
llmaker stop / start / rm       # lifecycle management

# ── Consume it — the agent's API, or any OpenAI client ──────────
AGENT=$(llmaker service ls --json | jq -r '.[]|select(.service=="agent").url')
curl "$AGENT/api/ingest"    -F file=@handbook.pdf            # add knowledge
curl "$AGENT/api/chat"      -d '{"question":"refund policy?"}'   # grounded answer + sources
curl "$AGENT/api/recommend" -d '{"like":["sku1","sku2"]}'   # semantic recommendations
```

[Self-Hosting LLMs Using Ollama and Docker](https://www.opensourceforu.com/2026/07/self-hosting-llms-using-ollama-and-docker/)

