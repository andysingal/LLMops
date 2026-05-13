An agent in the context of LLM orchestration is an intelligent controller that: 

- Receives a goal or task (for example, answer a user question, analyze a dataset, book a meeting on my calendar)
- Dynamically decides which actions to take next (which tools or subroutines to call) based on the current context and the outputs of previous steps
- Monitors its own progress, and re-planning as necessary

[source1](https://volumes.blog/2025/01/08/execution-guardrails-for-ai-agentic-implementation/)


[Agent Squad](https://github.com/awslabs/agent-squad)

Flexible, lightweight open-source framework for orchestrating multiple AI agents to handle complex conversations.

[gastown](https://github.com/gastownhall/gastown)

Gas Town is a workspace manager that lets you coordinate multiple AI coding agents (Claude Code, GitHub Copilot, Codex, Gemini, and others) working on different tasks. Instead of losing context when agents restart, Gas Town persists work state in git-backed hooks, enabling reliable multi-agent workflows.
