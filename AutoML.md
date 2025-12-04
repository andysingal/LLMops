[Automated GenAI](https://domino.ai/resources/blueprints/automated-genai-tracing-for-agent-and-llm-experimentation)

```
# config.yaml
models:
  openai: gpt-4o-mini
  anthropic: claude-sonnet-4-20250514

agents:
  classifier:
    temperature: 0.3
    max_tokens: 500
  response_drafter:
    temperature: 0.7
    max_tokens: 1500
```
