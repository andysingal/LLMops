[Building a Self-Improving Personal Knowledge Base Powered by LLM](https://louiswang524.github.io/blog/llm-knowledge-base/)

- 1. Raw storage — everything you ingest goes into raw/. Web articles, PDFs, images, notes. Nothing is processed here; it’s just a staging area. You feed this layer.

- 2. The wiki — a compiled, LLM-managed collection of markdown files in Obsidian format. Every concept gets its own article. Every source gets a summary. Everything is linked with Obsidian [[wikilinks]]. The LLM owns this layer entirely.

- 3. Outputs — Q&A answers, synthesis reports, lint reports, slides, charts. These get filed back into the wiki so future queries can reference them.

[New Video: Obsidian + Karpathy = 95% Cheaper “RAG” in Claude Code](https://www.skool.com/ai-automation-society/new-video-obsidian-karpathy-95-cheaper-rag-in-claude-code?p=05c35a3d)

[llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)

[claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler)
Adapted from Karpathy's LLM Knowledge Base architecture, but instead of clipping web articles, the raw data is your own conversations with Claude Code. When a session ends (or auto-compacts mid-session), Claude Code hooks capture the conversation transcript and spawn a background process that uses the Claude Agent SDK to extract the important stuff - decisions, lessons learned, patterns, gotchas - and appends it to a daily log. You then compile those daily logs into structured, cross-referenced knowledge articles organized by concept. Retrieval uses a simple index file instead of RAG - no vector database, no embeddings, just markdown.

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

## Articles
[When Your AI Wiki Outgrows the Context Window — A Practical Guide to RAG](https://dev.to/zaferdace/when-your-ai-wiki-outgrows-the-context-window-a-practical-guide-to-rag-kc2)

[Schema-First Extraction for LLM Wikis with GLiNER2](https://blog.veristamp.in/blog/schema-first-llm-wiki/?fbclid=IwY2xjawRJDDZleHRuA2FlbQIxMABicmlkETFGRmZheEtWanlra1pEVWpYc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHgp5i7fflHMhlgIDqdgiw_SkxfVVrdMWV2Mi_gy2Y6FaTXUG94onQz0-TyNT_aem_F3OzrCi9FoQR0iL7-Nrm1Q)
