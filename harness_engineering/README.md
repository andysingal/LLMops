Harness engineering is about building a complete working environment around the model so it produces reliable results. It's not about writing better prompts. It's about designing the system the model operates inside.
```
    ┌─────────────────────────────────────────────────────────────────┐
    │                        THE HARNESS                              │
    │                                                                 │
    │   ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐ │
    │   │ Instructions  │  │    State     │  │   Verification       │ │
    │   │              │  │              │  │                      │ │
    │   │ AGENTS.md    │  │ progress.md  │  │ tests + lint         │ │
    │   │ CLAUDE.md    │  │ feature_list │  │ type-check           │ │
    │   │ feature_list │  │ git log      │  │ smoke runs           │ │
    │   │ docs/        │  │ session hand │  │ e2e pipeline         │ │
    │   └──────────────┘  └──────────────┘  └──────────────────────┘ │
    │                                                                 │
    │   ┌──────────────┐  ┌──────────────────────────────────────┐   │
    │   │    Scope     │  │         Session Lifecycle             │   │
    │   │              │  │                                      │   │
    │   │ one feature  │  │ init.sh at start                     │   │
    │   │ at a time   │  │ clean-state checklist at end          │   │
    │   │ definition   │  │ handoff note for next session        │   │
    │   │ of done      │  │ commit only when safe to resume      │   │
    │   └──────────────┘  └──────────────────────────────────────┘   │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘

    The MODEL decides what code to write.
    The HARNESS governs when, where, and how it writes it.
    The harness doesn't make the model smarter.
    It makes the model's output reliable.

   
    ### RESOURCE
    -[Harness_engineering](https://github.com/walkinglabs/learn-harness-engineering)
        WITHOUT HARNESS                          WITH HARNESS
    ==============                          ============

    Session 1: agent writes code            Session 1: agent reads instructions
              agent breaks tests                      agent runs init.sh
              agent says "done"                       agent works on one feature
              you fix it manually                     agent verifies before claiming done
                                                       agent updates progress log
    Session 2: agent starts fresh                    agent commits clean state
              agent has no memory
              of what happened before         Session 2: agent reads progress log
              agent re-does work                       agent picks up exactly where it left off
              or does something else entirely          agent continues the unfinished feature
              you fix it again                         you review, not rescue

    Result: you spend more time                  Result: agent does the work,
            cleaning up than if you                      you verify the result
            did it yourself

```

    
    
 ## articles
[Meta-Harness - Automated model harness optimization, explained clearly](https://x.com/neural_avb/status/2039709486538260583)

[Harness_training_loop](https://x.com/Vtrivedy10/status/2039872562662941118)

[12 Agentic Harness Patterns from Claude Code](https://generativeprogrammer.com/p/12-agentic-harness-patterns-from)

[Better Harness: A Recipe for Harness Hill-Climbing with Evals](https://x.com/Vtrivedy10/status/2041927488918413589)

[Your harness, your memory](https://x.com/hwchase17/status/2042978500567609738)

<img width="551" height="426" alt="Screenshot 2026-04-11 at 5 40 04 PM" src="https://github.com/user-attachments/assets/639531fd-3436-46fa-ad12-c726bf2044a2" />


[Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents)

<img width="708" height="678" alt="Screenshot 2026-04-10 at 9 38 03 AM" src="https://github.com/user-attachments/assets/6c226a43-057b-47b0-9165-6bf4d5e95df2" />

<img width="643" height="595" alt="Screenshot 2026-04-10 at 9 34 23 AM" src="https://github.com/user-attachments/assets/5e2afc97-75b1-4a43-808c-2fdd4bd2e21f" />

[source_1](https://levelup.gitconnected.com/agent-harness-is-just-system-design-with-a-new-name-d91be4a648c5)


<img width="628" height="700" alt="Screenshot 2026-04-10 at 10 44 52 AM" src="https://github.com/user-attachments/assets/9f8da31c-edbd-42c5-86a1-1c088069a23c" />

[source_2](https://x.com/akshay_pachaar/status/2042586319390674994/photo/1)



<img width="555" height="299" alt="Screenshot 2026-04-10 at 12 12 02 PM" src="https://github.com/user-attachments/assets/411bd304-1a71-4e7c-8509-135e724d2907" />



[Meta-harness](https://github.com/stanford-iris-lab/meta-harness)

<img width="4744" height="1384" alt="repo" src="https://github.com/user-attachments/assets/2e6adfc9-3b3e-4b7d-a925-146fda77984a" />

Meta-Harness is a framework for automated search over task-specific model harnesses: the code around a fixed base model that decides what to store, retrieve, and show while the model works.

[EvoForge: Scaling Evolutionary Harness Optimization](https://x.com/leonardtang_/status/2044426476632629545)

[Resolvers: The Routing Table for Intelligence](https://x.com/garrytan/status/2044479509874020852)
A resolver is a routing table for context. When task type X appears, load document Y first. That's it. One sentence.



[Hermes Agent Stack](https://www.reddit.com/r/hermesagent/comments/1sj8hyw/llm_cheatsheet_for_hermes_agent/#lightbox)

<img width="1123" height="716" alt="Screenshot 2026-04-15 at 5 16 27 PM" src="https://github.com/user-attachments/assets/7ae60455-ea8a-4a52-84ed-783d7b4639db" />




### Articles 
[Harnesses are everything. Here's how to optimize yours](https://x.com/thealexker/status/2045203785304232162)

<img width="1241" height="480" alt="Screenshot 2026-04-18 at 11 35 34 AM" src="https://github.com/user-attachments/assets/fd651adc-3fb4-4cb7-b379-e13ab0514f7b" />

