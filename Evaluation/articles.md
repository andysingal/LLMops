[Five dimensions of validation](https://cloudsecurityalliance.org/blog/2026/07/02/validating-llm-generated-control-mappings-beyond-aggregate-accuracy)

- Coherence: Coherence measures whether the LLM agrees with domain experts, using chance-corrected kappa rather than raw accuracy.
- Consistency: Every taxonomy has structural constraints. Categories require specific subcategories. Some combinations are logically impossible. Parent-child relationships must be respected. These checks are entirely deterministic.
- Convergent validity: Convergent validity asks whether independent methods of measuring the same thing produce the same result.
- Adversarial discrimination: This dimension separates a classifier that understands the taxonomy from one that pattern-matches on vocabulary.
- Stability and sensitivity:
  - Stability measures whether rephrasing a control without changing its meaning preserves the classification.
  - Sensitivity measures whether changing the control description in a way that should change the classification actually does so. 
