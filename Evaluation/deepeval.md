[How we build evals for Deep Agents](https://x.com/Vtrivedy10/status/2037203679997018362)

When building Deep Agents, we catalog the behaviors that matter in production, such as retrieving content across multiple files in the filesystem or accurately composing 5+ tool calls in sequence. Rather than using benchmark tasks in aggregate, we take the following approach to eval curation:
- Decide which behaviors we want our agent to follow. Then research and curate targeted evals that measure those behaviors in a verifiable way.
- For each eval, add a docstring that explains how it measures an agent capability. This ensures each eval is self-documenting. We also tag each eval with categories like tool_use to enable grouped runs.
- Review output traces to understand failure modes and update eval coverage.
