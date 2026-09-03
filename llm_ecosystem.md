<img width="684" height="682" alt="Screenshot 2026-09-03 at 9 38 31 AM" src="https://github.com/user-attachments/assets/a5e59d48-3643-4b08-875d-a7bdca53b942" />

[langchain_echosystem](https://github.com/sysdr/langchain-echosystem/blob/main/backend/app/routes/threads.py)

### Article

[Building a Research Chat App on LangChain Managed Deep Agents (With Human Approval Before Web Search)](https://systemdr.systemdrd.com/p/building-a-research-chat-app-on-langchain?hide_intro_popup=1)

- backend/scripts/provision_agent.py reads everything under agent/, builds a JSON payload (instructions, tools, subagents, skills), POSTs or PATCHes the Managed Deep Agents API, and writes MANAGED_AGENT_ID back into .env.
- How a message travels through the system
You (browser)

→ POST /api/conversations (new thread_id)

→ POST /api/chat/stream (SSE: tokens + maybe interrupt)

→ [optional] POST resolve-interrupt

→ [optional] POST resume-stream (more SSE tokens)




