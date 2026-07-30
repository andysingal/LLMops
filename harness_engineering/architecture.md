An LLM is a neural network trained to predict the next token. It takes a sequence of tokens as input and produces a sequence of tokens as output. It cannot run a shell command, edit a file, or remember anything between calls. But an agent task like “fix this bug and run the tests” is mostly actions. Something has to turn the model’s predicted tokens into real commands, feed the results back, and continue until the task is done.

That is the job of the harness layer, a system built on top of the LLM to handle those responsibilities. It takes the user’s task as input, decides which instructions, which tool definitions, and how much history to include in the context, and maintains the conversation history. When the model responds with a tool call, the harness executes it under approval policies in a sandbox environment, appends the result, and sends the conversation back to the LLM.

<img width="492" height="265" alt="Screenshot 2026-07-30 at 12 49 40 PM" src="https://github.com/user-attachments/assets/26150efa-8da8-48ae-9eff-14f7ebccfd0c" />

<img width="1538" height="578" alt="Screenshot 2026-07-30 at 12 46 30 PM" src="https://github.com/user-attachments/assets/e87db2f9-a2e6-4a9c-a554-1330b140a554" />

The harness assembles instructions, tool definitions, and your task into a request and sends it to the API.
- The API buffers the request into memory, parses the JSON, and validates it: the request is well-formed, and the chosen model supports every feature it asks for. It checks who is calling, applies rate limits, and runs preflight checks.
- The API renders the conversation into the model’s input format and tokenizes it.
- The API dispatches the tokens to the inference layer, and starts its safety checks at the same time: classifiers that look for things like cyberattacks and bioweapon content. The safety checks race to finish before the first generated token comes back.
- The inference layer processes the prompt and begins generating. Its output here is not the final answer; it is a tool call: search the code for “checkout timeout.”
- The generated tokens flow back to the API
- The API converts tokens into text, wraps them in API events
- The API streams them to the harness.
- The harness recognizes the tool call, runs the search in its sandbox, appends the output to the conversation, and sends the updated conversation back to the API.

<img width="492" height="419" alt="Screenshot 2026-07-30 at 12 53 24 PM" src="https://github.com/user-attachments/assets/8e4bfacd-0f1f-48ae-866f-9a524f03141f" />
