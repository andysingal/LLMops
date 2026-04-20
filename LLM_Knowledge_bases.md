[Building a Self-Improving Personal Knowledge Base Powered by LLM](https://louiswang524.github.io/blog/llm-knowledge-base/)

- 1. Raw storage — everything you ingest goes into raw/. Web articles, PDFs, images, notes. Nothing is processed here; it’s just a staging area. You feed this layer.

- 2. The wiki — a compiled, LLM-managed collection of markdown files in Obsidian format. Every concept gets its own article. Every source gets a summary. Everything is linked with Obsidian [[wikilinks]]. The LLM owns this layer entirely.

- 3. Outputs — Q&A answers, synthesis reports, lint reports, slides, charts. These get filed back into the wiki so future queries can reference them.

[New Video: Obsidian + Karpathy = 95% Cheaper “RAG” in Claude Code](https://www.skool.com/ai-automation-society/new-video-obsidian-karpathy-95-cheaper-rag-in-claude-code?p=05c35a3d)

[llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)

[claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler)
Adapted from Karpathy's LLM Knowledge Base architecture, but instead of clipping web articles, the raw data is your own conversations with Claude Code. When a session ends (or auto-compacts mid-session), Claude Code hooks capture the conversation transcript and spawn a background process that uses the Claude Agent SDK to extract the important stuff - decisions, lessons learned, patterns, gotchas - and appends it to a daily log. You then compile those daily logs into structured, cross-referenced knowledge articles organized by concept. Retrieval uses a simple index file instead of RAG - no vector database, no embeddings, just markdown.


[AI Knowledge Layer (and why your agents are useless without it)](https://x.com/shannholmberg/status/2044111115878326444)

<img width="522" height="548" alt="Screenshot 2026-04-15 at 1 01 13 PM" src="https://github.com/user-attachments/assets/7f7dbcd4-1d4a-4ef1-89da-f37809352e1e" />

+-------------------------------------------------------+
|                    YOUR AGENTS                         |
|  (writer, researcher, strategist, analyst)             |
+---------------------------+---------------------------+
      |  reads from                  |  reads from
      v                              v
+------------------+   +-------------------+
|  KNOWLEDGE BASE  |   | BRAND FOUNDATION  |
|  LAYER (KBL)     |   | (BF)              |
|                  |   |                   |
|  dynamic         |   |  static           |
|  agent-maintained|   |  human-edited     |
|  grows over time |   |  your voice, your |
|  wiki pages,     |   |  rules, your      |
|  sources, index  |   |  positioning      |
+--------+---------+   +-------------------+
      |
compiles from
      |
+--------+---------+
|     raw/ inbox    |
|  tweets, articles |
|  bookmarks, PDFs  |
|  notes, ideas     |
+-------------------+




[memoriki](https://github.com/AyanbekDos/memoriki)
Personal knowledge base with real memory. Combines LLM Wiki (Andrej Karpathy) + MemPalace (MCP server).

Wiki gives structure. MemPalace gives memory.

```
# 1. Clone
git clone https://github.com/AyanbekDos/memoriki.git my-knowledge-base
cd my-knowledge-base

# 2. Install MemPalace
pip install mempalace
mempalace init .

# 3. Connect MemPalace to Claude Code
claude mcp add mempalace -- python -m mempalace.mcp_server

# 4. Drop your first source
cp ~/some-article.md raw/

# 5. Launch Claude Code and start ingesting
claude
# > Read raw/some-article.md and ingest it into the wiki
```

<img width="579" height="686" alt="Screenshot 2026-04-18 at 6 10 04 AM" src="https://github.com/user-attachments/assets/f6c5ae9e-9265-4cf1-87fa-02f932b845d2" />


## Articles
[When Your AI Wiki Outgrows the Context Window — A Practical Guide to RAG](https://dev.to/zaferdace/when-your-ai-wiki-outgrows-the-context-window-a-practical-guide-to-rag-kc2)

[Schema-First Extraction for LLM Wikis with GLiNER2](https://blog.veristamp.in/blog/schema-first-llm-wiki/?fbclid=IwY2xjawRJDDZleHRuA2FlbQIxMABicmlkETFGRmZheEtWanlra1pEVWpYc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHgp5i7fflHMhlgIDqdgiw_SkxfVVrdMWV2Mi_gy2Y6FaTXUG94onQz0-TyNT_aem_F3OzrCi9FoQR0iL7-Nrm1Q)

[LLM_Wiki_v2](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2)

[swarmvault](https://github.com/swarmclawai/swarmvault)

[llm_wiki](https://github.com/nashsu/llm_wiki)
A personal knowledge base that builds itself.
LLM reads your documents, builds a structured wiki, and keeps it current.



##### Useful repos
[OpenKB — Open LLM Knowledge Base](https://github.com/VectifyAI/OpenKB)

OpenKB (Open Knowledge Base) is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by PageIndex for vectorless long document retrieval.

```
raw/                              You drop files here
 │
 ├─ Short docs ──→ markitdown ──→ LLM reads full text
 │                                     │
 ├─ Long PDFs ──→ PageIndex ────→ LLM reads document trees
 │                                     │
 │                                     ▼
 │                         Wiki Compilation (using LLM)
 │                                     │
 ▼                                     ▼
wiki/
 ├── index.md            Knowledge base overview
 ├── log.md              Operations timeline
 ├── AGENTS.md           Wiki schema (LLM instructions)
 ├── sources/            Full-text conversions
 ├── summaries/          Per-document summaries
 ├── concepts/           Cross-document synthesis ← the good stuff
 ├── explorations/       Saved query results
 └── reports/            Lint reports
```
 [obsidian-llm-wiki](https://github.com/kytmanov/obsidian-llm-wiki-local)

 Turn your raw notes into a self-improving, interlinked wiki — powered by a local LLM.

Drop a markdown file into a folder. The pipeline reads it, extracts concepts, and creates or updates wiki articles with the new knowledge. Reject a draft and explain why — the next compile addresses your feedback. Over time your wiki compounds: every note you add (and every draft you review) makes the whole smarter.

Local-first, provider-flexible. Runs 100% locally with Ollama by default. Also works with any OpenAI-compatible endpoint — Groq, Together AI, LM Studio, vLLM, Azure OpenAI, and more.
