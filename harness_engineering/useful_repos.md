[browser_harness](https://github.com/browser-use/browser-harness)

Browser-harness takes the opposite path:
- · No capability encapsulation: It only provides a websocket connection to Chrome, allowing the LLM to send [CDP commands directly](https://x.com/shao__meng/status/2045657138119549006)
- · No preset flows: There are no scripts like "wait for element → click → input"; the LLM decides for itself how to interact with the page
- · No middleware: There's just a thin layer that translates the LLM's output into a protocol the browser can understand

<img width="793" height="623" alt="Screenshot 2026-04-19 at 9 51 38 PM" src="https://github.com/user-attachments/assets/1898aacd-c515-42ff-afd9-27c7f71e8bee" />
