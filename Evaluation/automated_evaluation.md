[Towards Automating Eval Engineering](https://www.langchain.com/blog/towards-automating-eval-engineering)

- Today we’re launching the Eval Engineering Skill, a skill that helps coding agents build evals using context from a repository and agent traces.
- The skill inspects how an agent is structured, mines patterns from traces if available, and proposes abilities to test.

<img width="767" height="287" alt="Screenshot 2026-07-30 at 9 22 05 AM" src="https://github.com/user-attachments/assets/1dbaeee2-6639-4633-ac95-652aa5f0e0c5" />

- We found that while agents are sometimes able to one-shot evals, the best evals came from users providing feedback and specifying which capabilities were worth measuring in agents.

```
The skill builds evals as Harbor tasks:

An Instruction: the message given to the agent at start describing the task
An environment: given as a Dockerfile containing the setup for the task such as what tools to install or what data to populate in the filesystem
A verifier that scores whether the agent completed the task correctly.

```

- Continual learning can be thought of as a continuous data mining problem where production data is used to build evals that improve agents over time. Teams mine traces to find recurring user requests, errors, failed tool calls, and incorrect state changes. which become evals so the same behavior can be measured and prevented in the future.

- ```
  mine traces -> identify a failure -> build an eval -> improve the agent -> rerun

  ```

  ```
  Use the eval-engineering skill to create an eval with me. Inspect the agent first, propose a few abilities worth testing, recommend one, and wait for me to choose.

  ```

  
