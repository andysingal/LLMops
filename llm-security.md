[Tinyauth](https://github.com/steveiliop56/tinyauth)

Tinyauth is a simple authentication middleware that adds simple username/password login or OAuth with Google, Github and any generic OAuth provider to all of your docker apps. It is made for traefik but it can be extended to work with all reverse proxies like caddy and nginx.


[uth-langchain](https://auth0.com/blog/genai-tool-calling-build-agent-that-calls-gmail-securely-with-langgraph-vercelai-nextjs/)

Learn how to build a tool-calling AI agent using LangGraph, Vercel AI SDK, and Next.js. Integrate different kinds of tools in them. Use Google services like Gmail, Calendar, and Drive as tools secured using Auth0 Token Vault.

[LlamaFirewall](https://www.xugj520.cn/en/archives/ai-security-framework-llamafirewall.html)

LlamaFirewall is an open-source security-focused guardrail framework designed to serve as a final layer of defense against security risks associated with AI agents. Unlike traditional moderation tools that mainly focus on filtering toxic content, LlamaFirewall provides system-level defenses tailored to modern agentic use cases, such as code generation, tool orchestration, and autonomous decision-making. It consists of a set of scanners for different security risks, including PromptGuardScanner, AlignmentCheckScanner, CodeShieldScanner, and customizable regex filters.

Decepticon - Vibe Hacking Agent: [Vibe Hacking](https://github.com/PurpleAILAB/Decepticon/) is a new paradigm in Offensive Security defined by PurpleAILAB.

Unlike traditional red teaming methods that rely on manual execution, AI agents autonomously perform red teaming tasks in Vibe Hacking.

[defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)

Large language model agents — like those built on OpenClaw — can install skills, call MCP servers, execute code, and reach the network. Every one of those actions is an attack surface. A single malicious skill can exfiltrate data. A compromised MCP server can inject hidden instructions. Generated code can contain hardcoded secrets or command injection.

DefenseClaw is the enterprise governance layer for OpenClaw. It sits between your AI agents and the infrastructure they run on, enforcing a simple principle: nothing runs until it's scanned, and anything dangerous is blocked automatically.
```
┌─────────────────────────────────────────────────────────┐
│                       DefenseClaw                       │
│                                                         │
│  ┌───────────┐   ┌───────────────────────────────────┐  │
│  │           │   │       DefenseClaw Gateway         │  │
│  │    CLI    │   │                                   │  │
│  │  (Python) │   │  ┌─────────────────────────────┐  │  │
│  │           │   │  │        AI Gateway           │  │  │
│  │           │   │  └─────────────────────────────┘  │  │
│  │           │   │  ┌─────────────────────────────┐  │  │
│  │           │   │  │      Inspect Engine         │  │  │
│  │           │   │  └─────────────────────────────┘  │  │
│  │           │   │                                   │  │
│  └───────────┘   └─────────────────┬─────────────────┘  │
│                                    │                    │
│                           WS (v3) + REST                │
│                                    │                    │
│  ┌─────────────────────────────────┼─────────────────┐  │
│  │         NVIDIA OpenShell        │                 │  │
│  │                                 │                 │  │
│  │  ┌──────────────────────────────┴──────────────┐  │  │
│  │  │                  OpenClaw                   │  │  │
│  │  │                                             │  │  │
│  │  │  ┌───────────────────────────────────────┐  │  │  │
│  │  │  │     DefenseClaw Plugin (TS)           │  │  │  │
│  │  │  └───────────────────────────────────────┘  │  │  │
│  │  │                                             │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  │                                                   │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Few things to remember

-- Raw Power --> Versatile but unpredictable (bias, toxicity)
-- Guardrails Needed --> Filters, audits, security checks
-->Shared Risks --> Bias | Privacy leaks | Misuse
--> Unique App Risks --> Hallucinations | Off-topic rambles | Data leaks

### Customizing LLM Safety
Industry-Specific Risks - Zombie diagonoses | Leaky credit cards
Tools for Defense - OWASP Top 10 | AI Incident DB | AVID
Actions Steps --> Test | Filter | Learn from fails

## Key LLM Vulnerabilities
Bias & Streotypes --> Parrots repeating bad habbits
Sensitive Info Leaks - Diaries the AI shouldn't read
Service Disruption --> Hackers causing traffic jams
Hallucinations --> Creative storytellers

### Penetration Testing
-- Find & Map Weaknesses 


## Articles
[Guardrails as Architecture: Safe guarding GenAI apps](https://dev.to/arbitrarybytes/guardrails-as-architecture-safe-guarding-genai-apps-46pd)

[How to red team LLM Agents](https://www.promptfoo.dev/docs/red-team/agents/)

[How to de-identify PHI before it reaches your LLM](https://www.aptible.com/hipaa-ai-security/phi-deidentification)
