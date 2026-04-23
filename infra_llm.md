[coral](https://github.com/Human-Agent-Society/CORAL)

CORAL is an infrastructure for building organizations of autonomous AI agents that run experiments, share knowledge, and continuously improve solutions. Give it a codebase and a grading script, and Coral handles the rest: isolated workspaces, safe evaluation, persistent shared knowledge, and multi-agent collaboration to enable robust evolution. Coral is natively integrated with Claude Code, OpenCode, Codex, and other major coding agents.

```
# start a run
uv run coral start -c examples/kernel_builder/task.yaml

# override any config value via dotlist syntax
uv run coral start -c task.yaml agents.count=4 agents.model=opus
uv run coral start -c task.yaml run.verbose=true        # stream agent output
uv run coral start -c task.yaml run.ui=true              # also launch web dashboard
uv run coral start -c task.yaml run.session=local         # skip tmux, run inline
uv run coral start -c task.yaml run.session=docker        # run inside Docker container

# warm-start: research phase before coding (agents do literature review first)
uv run coral start -c task.yaml agents.warmstart.enabled=true agents.research=true

# stop and resume
uv run coral stop                                        # stop anytime
uv run coral resume                                      # pick up where you left off
uv run coral resume agents.model=opus run.verbose=true   # resume with overrides

# monitor progress
uv run coral ui                                          # open the web dashboard
```
