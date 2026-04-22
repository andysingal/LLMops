Context  engine follows a simple yet powerful rhythm: plan, execute, and reflect. It explains how to connect it to your agents using MCP, and how to design a reasoning system that’s scalable, transparent, and resilient.

how do we move from a collection of agents to an adaptive, autonomous system? That is where the Context Engine comes in.

The Context Engine is a meta-system, an intelligent controller that organizes specialized agents around a high-level goal. It is more than a single function; it is a structured workflow that turns a vague intent into a grounded, context-aware output. While our label “Context Engine” is specific to this framework, the pattern is widely used in advanced generative AI platforms. Systems such as ChatGPT or Gemini are not single models in isolation. They are applications with controllers that manage sessions, orchestrate tools, and maintain context. Conceptually, those controllers play the same role as a Context Engine.

Context Engine employs a two-phase process:

- First, a Planner acts as the strategic core, reasoning about the user's goal in using the Agent Registry as a "toolkit" of available capabilities to select the best agent or function. We will thus build these new additional Planner and Agent Registry tools in this chapter.
- Then, the Planner uses an LLM to generate a dynamic, step-by-step execution plan tailored to the specific task. Once the plan is ready, it is handed off to an Executor, the operational manager who invokes the specialist agents in the correct sequence.


<img width="532" height="468" alt="Screenshot 2026-04-02 at 3 48 00 PM" src="https://github.com/user-attachments/assets/81a58a7a-8147-436e-a16d-debfb1ebac60" />

### Architectural overview
The Context Engine is a dynamic, multi-stage workflow, as shown in the diagram. Each color represents a distinct functional layer that collaborates <u>to transform a high-level goal into a fully generated output</u>.

- Planner: The strategic core that receives the user’s goal and designs a step-by-step plan.
- Executor: The operational manager that carries out the plan, calling specialized agents and managing the data flow between them.
- Tracer: The transparent recorder that logs every action for debugging and insight.

Context Engine employs a two-phase process:
- First, a Planner acts as the strategic core, reasoning about the user's goal in using the Agent Registry as a "toolkit" of available capabilities to select the best agent or function. We will thus build these new additional Planner and Agent Registry tools in this chapter.
- Then, the Planner uses an LLM to generate a dynamic, step-by-step execution plan tailored to the specific task. Once the plan is ready, it is handed off to an Executor, the operational manager who invokes the specialist agents in the correct sequence.

The second phase is execution, where the Executor coordinates the green Specialist Agents and external red services. Following the plan step by step, it calls on the following:

- The Librarian handles procedural RAG to fetch stylistic blueprints.
- The Researcher performs factual RAG to gather and synthesize relevant information.
- The Writer combines style and facts to produce the final content.


*** Each of these agents interacts with external services. The Librarian and Researcher query the Vector DB, while the Researcher and Writer may call the LLM to refine facts or generate text.

This standardization is what enables context chaining. Each agent receives an MCP message as input and returns another as output, allowing the Executor to simply pass along the data without worrying about translation or formatting. This seamless flow of information is what makes stateful, multi-step reasoning possible and is the foundation upon which the entire engine operates.




The second phase is execution, where the Executor coordinates the green Specialist Agents and external red services. Following the plan step by step, it calls on the following:

- The Librarian handles procedural RAG to fetch stylistic blueprints.
- The Researcher performs factual RAG to gather and synthesize relevant information.


###### Context Librarian agent

```
 === 4.1. Context Librarian Agent (Procedural RAG) ===
def agent_context_librarian(mcp_message):
    """
    Retrieves the appropriate Semantic Blueprint from the Context Library.
    """
    print("\n[Librarian] Activated. Analyzing intent...")
    # Extract the specific input required by this agent
    requested_intent = mcp_message['content'].get('intent_query')

    if not requested_intent:
        raise ValueError("Librarian requires 'intent_query' in the input content.")

    # Query Pinecone Context Namespace
    results = query_pinecone(requested_intent, NAMESPACE_CONTEXT, top_k=1)

    if results:
        match = results[0]
        print(f"[Librarian] Found blueprint '{match['id']}' (Score: {match['score']:.2f})")
        # Retrieve the blueprint JSON string stored in metadata
        blueprint_json = match['metadata']['blueprint_json']
        # The output content IS the blueprint itself (as a string)
        content = blueprint_json
    else:
        print("[Librarian] No specific blueprint found. Returning default.")
        # Fallback default
        content = json.dumps({"instruction": "Generate the content neutrally."})

    return create_mcp_message("Librarian", content)
```

##### === 4.2. Researcher Agent (Factual RAG) ===
```
def agent_researcher(mcp_message):
    """
    Retrieves and synthesizes factual information from the Knowledge Base.
    """
    print("\n[Researcher] Activated. Investigating topic...")
    # Extract the specific input required by this agent
    topic = mcp_message['content'].get('topic_query')

    if not topic:
        raise ValueError("Researcher requires 'topic_query' in the input content.")

    # Query Pinecone Knowledge Namespace
    results = query_pinecone(topic, NAMESPACE_KNOWLEDGE, top_k=3)

    if not results:
        print("[Researcher] No relevant information found.")
        # Return a string indicating no data found
        return create_mcp_message("Researcher", "No data found on the topic.")

    # Synthesize the findings (Retrieve-and-Synthesize)
    print(f"[Researcher] Found {len(results)} relevant chunks. Synthesizing...")
    source_texts = [match['metadata']['text'] for match in results]

    system_prompt = """You are an expert research synthesis AI.
    Synthesize the provided source texts into a concise, bullet-pointed summary relevant to the user's topic. Focus strictly on the facts provided in the sources. Do not add outside information."""

    user_prompt = f"Topic: {topic}\n\nSources:\n" + "\n\n---\n\n".join(source_texts)

    # Use a low temperature for factual synthesis
    findings = call_llm_robust(system_prompt, user_prompt)

    # The output content IS the findings (as a string)
    return create_mcp_message("Researcher", findings)

```

#### # === 4.3. Writer Agent (Generation) ===
```
def agent_writer(mcp_message):
    """
    Combines the factual research with the semantic blueprint to generate the final output.
    Crucially enhanced to handle either raw facts OR previous content for rewriting tasks.
    """
    print("\n[Writer] Activated. Applying blueprint to source material...")

    # Extract inputs.
    blueprint_json_string = mcp_message['content'].get('blueprint')
    # Check for 'facts' first, then 'previous_content'
    facts = mcp_message['content'].get('facts')
    previous_content = mcp_message['content'].get('previous_content')

    if not blueprint_json_string:
         raise ValueError("Writer requires 'blueprint' in the input content.")

    # Determine the source material and label for the prompt
    if facts:
        source_material = facts
        source_label = "RESEARCH FINDINGS"
    elif previous_content:
        source_material = previous_content
        source_label = "PREVIOUS CONTENT (For Rewriting)"
    else:
        raise ValueError("Writer requires either 'facts' or 'previous_content'.")

```


- The Writer combines style and facts to produce the final content.

