[HALO](https://github.com/context-labs/halo)
HALO (Hierarchical Agent Loop Optimization) is a methodology for building recursively self-improving agent harnesses using RLMs. 

<img width="1448" height="1086" alt="halo-rlm" src="https://github.com/user-attachments/assets/7bd1e5cc-f0ff-4733-af74-cefe080ecb74" />

A single user request may involve:

- Multiple agents
- Tool calls
- Retrieval pipelines
- MCP servers
- Several LLM invocations
- Conditional graph routing
When something goes wrong, developers need visibility into what happened.

Today, the most common solution is to add logging everywhere, inspect terminal output, or integrate a full observability platform.

But what if you just want to see what your agent is doing right now?

That’s the problem [Tracesage](https://forum.langchain.com/t/tracesage-see-inside-your-langgraph-agents/4063) was built to solve.

