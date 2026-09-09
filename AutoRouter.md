One router for complexity, semantic, and adaptive routing. Classify each request with heuristics, an LLM classifier, lexical/semantic keyword rules, or your own classifier plugin, then route to a pinned model, a random pool, or a Thompson-sampled pool per tier.

```
- model_name: smart-router
  litellm_params:
    model: auto_router/complexity_router
    drop_params: true
    complexity_router_config:
      tiers:
        SIMPLE:    ["gpt-5.6-luna", "gemini-3.8-flash"]   # random-pick pool
        MEDIUM:    gpt-5.6-terra                                 # single pin
        COMPLEX:   claude-sonnet-5
        REASONING: claude-opus-5

      # Optional display names; omit to keep SIMPLE/MEDIUM/COMPLEX/REASONING everywhere
      # tier_labels:
      #   SIMPLE: Cheap

      # LLM classifier instead of the heuristic scorer
      classifier_type: llm
      classifier_llm_config:
        model: claude-sonnet-5
        timeout_ms: 2000
        # system_prompt: <your rubric>         # replaces the built-in rubric entirely; omit for the default
      classifier_fallback: heuristic           # default; or default_model
      # Prior conversation the classifier sees (LLM classifier only)
      classifier_context_window_size: 3          # default 3; 0 disables
      classifier_context_per_turn_chars: 200     # default 200
      classifier_context_include_assistant_turns: false   # default false

      # Or hand the tier decision to your own code (config file only)
      # classifier_type: custom
      # classifier_plugin: classifiers.tier_by_team   # dotted path to an async classify(context)
      # classifier_plugin_timeout_ms: 3000            # default

      # Keyword rules, run before the scorer, escalate to the highest matched tier
      keyword_tier_rules:
        - keywords: ["hi", "hello", "thanks"]
          tier: SIMPLE
        - keywords: ["kubernetes", "k8s", "istio"]
          tier: REASONING
      semantic_keyword_matching: true
      embedding_model: voyage-3-5
      match_threshold: 0.5

      # Append to the built-in technical keyword list
      custom_technical_keywords: [kafka, redis, postgresql, udp, dns]

      # Marker pair whose blocks are stripped before classification
      reminder_markers: ["<system-reminder>", "</system-reminder>"]   # default

      # Escalate a prompt that provably does not fit the decided tier, before dispatch
      enable_context_window_escalation: true   # default
      context_window_escalation_buffer: 0.95   # default; prompt must fit within this fraction of the window

      # Send image-bearing requests to a tier that can see them
      modality_routing: false   # default; set true to opt in

      # Classify new user asks only, carrying the decision through continuation turns
      classification_mode: every_request   # default; or user_turn

      # Thompson-sample within the tier's pool
      adaptive: true

      # Pin a session to its first-turn model to preserve prompt cache
      session_affinity: false   # default; set true to pin
      session_affinity_ttl_seconds: 3600

      # Return the model the router picked in the response body `model` field
      # instead of restamping it back to the alias the client called
      return_raw_model_name: false   # default

      # Tune heuristic scorer boundaries and weights (all optional)
      tier_boundaries:
        simple_medium:     0.15
        medium_complex:    0.35
        complex_reasoning: 0.60
      token_thresholds:
        simple:  15
        complex: 400
      dimension_weights:
        tokenCount:        0.10
        codePresence:      0.30
        reasoningMarkers:  0.25
        technicalTerms:    0.25
        simpleIndicators:  0.05
        multiStepPatterns: 0.03
        questionComplexity: 0.02

    complexity_router_default_model: claude-sonnet-5

    # Compression guardrail per hop; a guardrail name, or `none`. Both unset (the
    # default) keeps whatever compression the key, team, or request already applies
    # on both hops
    # auto_router_routing_compression: headroom-compression
    # auto_router_model_compression: none
```
[Autoscaler_litellm](https://docs.litellm.ai/docs/proxy/auto_routing)

