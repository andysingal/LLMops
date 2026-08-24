<img width="632" height="239" alt="Screenshot 2026-08-24 at 1 04 33 PM" src="https://github.com/user-attachments/assets/c84fed01-27da-40af-a497-71d667cabd92" />

```py
import llm_verifier

problem = "Write a function that reverses a string."
candidates = [
    "def rev(s): return s[::-1]", "def rev(s): return s", "def rev(s): return ''.join(sorted(s))",
]

result = llm_verifier.select(
    problem=problem,
    candidates=candidates,
    criteria={"Correctness": "Does the code actually reverse the string?"},
)
print(result.index)   # index of the best candidate: 0
print(result.scores)  # candidate scores: [0.73104, 0.38446, 0.38449]
```
