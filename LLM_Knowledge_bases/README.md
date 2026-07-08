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

[OmegaWiki](https://github.com/skyllwt/OmegaWiki)

Andrej Karpathy proposed LLM-Wiki: an LLM that builds and maintains a persistent, structured wiki from your sources — not a throwaway RAG answer, but compounding knowledge that grows smarter with every paper you feed it.

ΩmegaWiki takes that idea and runs the full distance. It's not just a wiki builder — it's a complete research lifecycle platform: from paper ingestion → knowledge graph → gap detection → idea generation → experiment design → paper writing → peer review response. All driven by 24 Claude Code skills, all centered on one wiki as the single source of truth.

Drop your .tex / .pdf files in a folder. Run one command. Get a fully cross-referenced knowledge base — and then use it to generate novel research ideas, design experiments, write papers, and respond to reviewers.



#### LLM Brain 

[meg_brain_decoding_neuralset_cnn_Marktechpost](https://www.marktechpost.com/2026/05/01/a-coding-implementation-of-end-to-end-brain-decoding-from-meg-signals-using-neuralset-and-deep-learning-for-predicting-linguistic-features/)


[Beyond RAG: Why Knowledge Engineering Becomes the Real Moat in the Agent Era](https://dev.to/seekdb/beyond-rag-why-knowledge-engineering-becomes-the-real-moat-in-the-agent-era-41c4)

And three core operations:

- Ingest: parse one new source, summarize, cross-link, update many pages.

- Query: answer from wiki pages (not just raw chunks), file high-value answers back as pages.

- Lint: periodically detect contradictions, stale claims, orphan pages, missing links.


[second-brain](https://github.com/henrydaum/second-brain)

Second Brain is an attempt to make a digital brain that approximates the real thing. It's part knowledge engine, part personal operator, and part programmable automation layer.

It continuously indexes your files, remembers durable context, searches the web when local knowledge is not enough, and runs tools and shell commands. It lives in your terminal and Telegram, so your assistant is available everywhere.

Instead of being "just a chatbot," it turns your machine into a system that can observe, search, reason, and act. Point it at your world, give it tools, and it becomes a private AI layer for research, reminders, recurring work, and everyday operations.


<img width="900" height="406" alt="Screenshot 2026-07-03 at 6 14 56 PM" src="https://github.com/user-attachments/assets/17293cf2-e3f1-4925-8073-a7183aa05129" />

<img width="924" height="360" alt="Screenshot 2026-07-03 at 6 16 19 PM" src="https://github.com/user-attachments/assets/96367b64-97f4-4256-8a21-ab8a82e1de73" />

<img width="885" height="399" alt="Screenshot 2026-07-03 at 6 17 18 PM" src="https://github.com/user-attachments/assets/f3201b3d-bab6-49d5-89cb-ec4d8556d98f" />

#### Perception
<img width="829" height="441" alt="Screenshot 2026-07-03 at 6 19 43 PM" src="https://github.com/user-attachments/assets/f4aa9dcb-f0c7-4589-b503-0998ec3be875" />

<img width="906" height="434" alt="Screenshot 2026-07-03 at 6 21 07 PM" src="https://github.com/user-attachments/assets/d5809dda-457a-458d-9526-d4a8ad577a76" />

<img width="885" height="452" alt="Screenshot 2026-07-03 at 6 25 04 PM" src="https://github.com/user-attachments/assets/e4ad6e52-66d7-4482-ba63-7db52b5ef946" />


<img width="855" height="545" alt="Screenshot 2026-07-04 at 3 34 02 PM" src="https://github.com/user-attachments/assets/d92c7795-ddd2-4533-a839-23e059850852" />

<img width="864" height="528" alt="Screenshot 2026-07-04 at 3 34 55 PM" src="https://github.com/user-attachments/assets/ada0f6bc-ba1e-4b2e-9a1b-a208f41082f5" />

<img width="905" height="441" alt="Screenshot 2026-07-04 at 3 36 32 PM" src="https://github.com/user-attachments/assets/93ac7266-7320-412a-97e2-777da96b9847" />

### memory
<img width="899" height="375" alt="Screenshot 2026-07-04 at 4 03 40 PM" src="https://github.com/user-attachments/assets/89a3e319-8269-4c43-adb5-19e77a956f20" />

<img width="904" height="413" alt="Screenshot 2026-07-04 at 4 05 24 PM" src="https://github.com/user-attachments/assets/3682328e-550e-41a2-b8cd-eec35be1f0f8" />

<img width="919" height="471" alt="Screenshot 2026-07-04 at 4 06 21 PM" src="https://github.com/user-attachments/assets/2a9530a3-e73a-42dc-b17b-c0c6ef123c1d" />

<img width="919" height="538" alt="Screenshot 2026-07-04 at 4 07 35 PM" src="https://github.com/user-attachments/assets/66f99824-6d28-4e5c-8ef3-5b6039e0e4f8" />

<img width="905" height="450" alt="Screenshot 2026-07-04 at 4 10 25 PM" src="https://github.com/user-attachments/assets/7705ed5f-6df4-4120-a738-d3e8d2f57fe6" />


### Action(Hands)

<img width="905" height="467" alt="Screenshot 2026-07-05 at 11 31 11 AM" src="https://github.com/user-attachments/assets/21103058-5e59-4cf4-8257-51325fed640f" />


### Tool:
A tool is any function , script, API or external system that the agent is given permission to execute

<img width="907" height="441" alt="Screenshot 2026-07-05 at 11 45 00 AM" src="https://github.com/user-attachments/assets/5f22fa65-e926-4f77-bf43-4c52c0046942" />


### Security and Guardrails
<img width="864" height="465" alt="Screenshot 2026-07-05 at 11 47 05 AM" src="https://github.com/user-attachments/assets/28b85244-1be5-4193-935c-1781ae118458" />

<img width="923" height="472" alt="Screenshot 2026-07-05 at 11 48 19 AM" src="https://github.com/user-attachments/assets/8c178712-0b07-49e1-885f-3c0606c95fef" />


### Feedback Loop(Learning)
<img width="934" height="430" alt="Screenshot 2026-07-05 at 12 01 55 PM" src="https://github.com/user-attachments/assets/62840d45-fcfd-4be1-956d-f14f7d0efa46" />

<img width="902" height="432" alt="Screenshot 2026-07-05 at 12 03 03 PM" src="https://github.com/user-attachments/assets/ba8ce410-d667-4c58-9618-2581acef252a" />

<img width="911" height="447" alt="Screenshot 2026-07-05 at 12 15 57 PM" src="https://github.com/user-attachments/assets/216a471e-cbbf-472a-9a94-cb49d8bb1fb0" />

### Voice Agent Communication 
<img width="869" height="465" alt="Screenshot 2026-07-05 at 12 25 50 PM" src="https://github.com/user-attachments/assets/12f0070b-c04a-4b2d-afb2-cc08dc2cdbb0" />

- Agent to Human Communication
<img width="908" height="416" alt="Screenshot 2026-07-05 at 12 28 01 PM" src="https://github.com/user-attachments/assets/e86667ac-413e-4e23-8468-4da61f176cdf" />

<img width="859" height="423" alt="Screenshot 2026-07-05 at 12 29 04 PM" src="https://github.com/user-attachments/assets/94d25291-afc3-4e87-80c4-0b9b95284a09" />


- Agent to Agent Communication

### Research Agent

<img width="913" height="467" alt="Screenshot 2026-07-05 at 12 38 13 PM" src="https://github.com/user-attachments/assets/8df264e9-4944-4ecd-9b0b-384ce2a3b5f2" />

<img width="881" height="460" alt="Screenshot 2026-07-05 at 12 39 17 PM" src="https://github.com/user-attachments/assets/71ce2446-08db-4951-a261-56ad283405d8" />


### System Prompt:
You are a Research Assistant. Your goal is to write a factual report based on user requests. You must use the web_search tool to gather information. You must not answer from your own knowledge. You must first search, then analyze the results,then write the final report.

Step II: This is a complex reasoning task, so we will choose a high-capability model (like GPT-5, Claude-4 or Gemini Advanced) that is excellenet at planning and function calling 

Step III : The Hands (Tool Definition)

<img width="910" height="525" alt="Screenshot 2026-07-05 at 5 26 33 PM" src="https://github.com/user-attachments/assets/b21a149a-cce1-429a-a041-02c019c8c377" />


Step 4: The "memory" (Tha scratchpad")

Short Term Memory: We will use a simple Python list to store the conversation history(chat_history=[]). This list will store both the user's messages and the results of our tool calls

Long Term Memory:
building an external database.
Our web_search tool simulates our agent accessing a vast Long Term Memory

The loop: 

<img width="920" height="423" alt="Screenshot 2026-07-05 at 5 46 48 PM" src="https://github.com/user-attachments/assets/578af993-70fc-445b-bf62-d4fcd5554c34" />


<img width="842" height="403" alt="Screenshot 2026-07-05 at 5 49 24 PM" src="https://github.com/user-attachments/assets/f0410649-9edf-4fc9-a023-5be77cc28037" />

Agentic Loop: Perception, Reasoning, Action, Learning 
<img width="864" height="463" alt="Screenshot 2026-07-05 at 6 04 11 PM" src="https://github.com/user-attachments/assets/c13c3e0d-d9fd-41e8-9bee-ffe35eca149b" />

<img width="879" height="459" alt="Screenshot 2026-07-05 at 6 17 46 PM" src="https://github.com/user-attachments/assets/40973db8-3683-4ee4-8c03-a1dd78404651" />

### Example

<img width="880" height="465" alt="Screenshot 2026-07-05 at 6 22 44 PM" src="https://github.com/user-attachments/assets/b6c078ff-6677-41dd-a66e-b333f53cb402" />

<img width="902" height="460" alt="Screenshot 2026-07-05 at 6 24 14 PM" src="https://github.com/user-attachments/assets/744f4186-f58c-4911-8c27-bbde54c85f81" />

<img width="885" height="431" alt="Screenshot 2026-07-05 at 6 26 09 PM" src="https://github.com/user-attachments/assets/75f52415-f2ba-455b-b004-54da519e1166" />


### Agentic AI

Multi-Agent System for Research + Article Writing

Behavior:
- Read a human-written article guarantee to understand the topic to rsearch - the more we define the agent's goal, the better
- Scrape user provided webpages, youtube videos and github repositories to gather more context
- Iteratively do web serches to learn more about the topic and gather material, following user feedback after each batch of web searches
- Revise all the gathered content and filter to keep only the most relevant and trustworthy content
- Write all the gathered content into a final artifcact, which will be used by the writer agent

Scraping solution: use Firecrawl + agentic scraping
- Websites block suspected bots -- scraping services can act like users and get to the webpage
- Websites work with HTML: scraping services can parse the HTML and extract the relevant content, which is not s straightforward task to make work on all websites
- Many websites are SPAs(single applications), content is often rendered dynamically

### Youtube videos
-Use Gemini to transcribe the video and describe it

### Github:
US the gitingest open source library which formats Github content into Markdown format that is easily understandable by LLMs


Orchestration(where is the full "recipe" of how to use the tools in sequence located?): It's defined in an MCP prompt.
- When the MCP client connects to MCP server, it can read the recipe of how to do the full research from an MCP prompt of the MCP server, and then MCP client will start using all the tools knowing how they work together

<img width="910" height="456" alt="Screenshot 2026-07-07 at 9 38 27 PM" src="https://github.com/user-attachments/assets/78813f20-4642-4eb6-bd2c-95d4d72432cb" />

### What is Multi-Agent System (MAS)

<img width="884" height="508" alt="Screenshot 2026-07-07 at 9 45 11 PM" src="https://github.com/user-attachments/assets/37464a75-5c59-400a-8def-a10b43877c2a" />

### Agent as a service

<img width="880" height="498" alt="Screenshot 2026-07-07 at 9 48 31 PM" src="https://github.com/user-attachments/assets/1ea737f1-6511-4f28-97b2-978b80302f1a" />


<img width="936" height="422" alt="Screenshot 2026-07-07 at 9 54 03 PM" src="https://github.com/user-attachments/assets/79cf4800-b1b6-404f-a413-d091973c7f98" />

## Primary Patterns for Agent Coordination

<img width="928" height="448" alt="Screenshot 2026-07-07 at 9 55 02 PM" src="https://github.com/user-attachments/assets/fc80ed54-e7f5-4f4f-b746-bb630e67d0a2" />

<img width="897" height="438" alt="Screenshot 2026-07-07 at 9 58 11 PM" src="https://github.com/user-attachments/assets/6e0a6cc3-3cd3-4b70-a029-cd583b17d00b" />

<img width="950" height="470" alt="Screenshot 2026-07-07 at 9 59 38 PM" src="https://github.com/user-attachments/assets/51530ad5-141c-40dc-be7e-478a15739745" />

<img width="907" height="443" alt="Screenshot 2026-07-07 at 10 00 39 PM" src="https://github.com/user-attachments/assets/8e940f27-52c6-4a75-8fcf-9a58eff19cc2" />

<img width="927" height="469" alt="Screenshot 2026-07-07 at 10 22 44 PM" src="https://github.com/user-attachments/assets/68d96e11-2f13-4efc-b7b1-ac9264741807" />

### Challenges of Agentic AI System

<img width="892" height="457" alt="Screenshot 2026-07-07 at 10 24 53 PM" src="https://github.com/user-attachments/assets/20eb5008-e973-45ed-b04e-7b7956e4ddb3" />

<img width="905" height="402" alt="Screenshot 2026-07-07 at 10 26 25 PM" src="https://github.com/user-attachments/assets/cb33677c-ab4c-429d-ac1b-9f8c1321d952" />

<img width="882" height="449" alt="Screenshot 2026-07-07 at 10 26 58 PM" src="https://github.com/user-attachments/assets/e5601c07-5dbe-4217-a7a5-4f499f1f732e" />

<img width="886" height="413" alt="Screenshot 2026-07-07 at 10 27 52 PM" src="https://github.com/user-attachments/assets/5c8d62a0-56f9-47ee-a84e-f6ec1f7462ae" />












