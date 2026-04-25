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


### The Context Engine

We’ve met the specialists and we’ve cataloged them in the Agent Registry. The next step is to make the whole team think and act as one. That is the job of the Context Engine.

At its heart, the engine runs a simple but powerful loop that mirrors how people work through complex problems: plan, execute, reflect. The Planner thinks strategically, breaking down a broad goal into a clear plan of steps. The Executor gets its hands dirty, carrying out that plan, calling the right agents at the right time, and passing context along as it evolves. The Execution Tracer plays the quiet but essential role of observer, recording every move so we can later see not just what the system did, but why it did it.



### Planner

We start with the planner function, the strategic core of the engine. It acts as an expert project manager, translating a vague, high-level human goal into a precise, step-by-step, machine-readable JSON plan. Its intelligence comes from its ability to use an LLM as a reasoning partner.

The Planner needs two things: the user’s goal and a capabilities description from the Agent Registry. With those in hand, it begins its analysis:

```
# === 6.2. The Planner (Strategic Analysis) ===
def planner(goal, capabilities):
    """
    Analyzes the goal and generates a structured Execution Plan using the LLM.
    """
    print("[Engine: Planner] Analyzing goal and generating execution plan...")
    system_prompt = f"""
    You are the strategic core of the Context Engine. Analyze the user's high-level goal and create a structured Execution Plan using the available agents.

    --- AVAILABLE CAPABILITIES ---
    {capabilities}
    --- END CAPABILITIES ---

    INSTRUCTIONS:
    1. The plan MUST be a JSON list of objects, where each object is a "step".
    2. You MUST use Context Chaining. If a step requires input from a previous step, reference it using the syntax 
STEP_X_OUTPUT
.
    3. Be strategic. Break down complex goals (like sequential rewriting) into distinct steps. Use the correct input keys ('facts' vs 'previous_content') for the Writer agent.

    EXAMPLE GOAL: "Write a suspenseful story about Apollo 11."
    EXAMPLE PLAN (JSON LIST):
    [
        {{"step": 1, "agent": "Librarian", "input": {{"intent_query": "suspenseful narrative blueprint"}}}},
        {{"step": 2, "agent": "Researcher", "input": {{"topic_query": "Apollo 11 landing details"}}}},
        {{"step": 3, "agent": "Writer", "input": {{"blueprint": "
STEP_1_OUTPUT
", "facts": "
STEP_2_OUTPUT
"}}}}
    ]

    EXAMPLE GOAL: "Write a technical report on Juno, then rewrite it casually."
    EXAMPLE PLAN (JSON LIST):
    [
        {{"step": 1, "agent": "Librarian", "input": {{"intent_query": "technical report structure"}}}},
        {{"step": 2, "agent": "Researcher", "input": {{"topic_query": "Juno mission technology"}}}},
        {{"step": 3, "agent": "Writer", "input": {{"blueprint": "
STEP_1_OUTPUT
", "facts": "
STEP_2_OUTPUT
"}}}},
        {{"step": 4, "agent": "Librarian", "input": {{"intent_query": "casual summary style"}}}},
        {{"step": 5, "agent": "Writer", "input": {{"blueprint": "
STEP_4_OUTPUT
", "previous_content": "
STEP_3_OUTPUT
"}}}}
    ]

    Respond ONLY with the JSON list.
    """
    # Call LLM in JSON mode for reliability
    plan_json = ""
    try:
        plan_json = call_llm_robust(system_prompt, goal, json_mode=True)
        plan = json.loads(plan_json)

        if not isinstance(plan, list):
             # Handle cases where the LLM wraps the list in a dictionary
             if isinstance(plan, dict):
                 if "plan" in plan and isinstance(plan["plan"], list):
                     plan = plan["plan"]
                 elif "steps" in plan and isinstance(plan["steps"], list): # <--- ADD THIS CHECK
                     plan = plan["steps"]
                 else:
                    raise ValueError("Planner returned a dict, but missing 'plan' or 'steps' key.")
             else:
                raise ValueError("Planner did not return a valid JSON list structure.")

        print("[Engine: Planner] Plan generated successfully.")
        return plan
    except Exception as e:
        print(f"[Engine: Planner] Failed to generate a valid plan. Error: {e}. Raw LLM Output: {plan_json}")
        raise e




```

With the briefing ready, the Planner calls the LLM to act as a reasoning partner. The entire process is wrapped in a robust try...except block to handle potential errors, such as malformed JSON from the LLM. After calling the LLM and parsing the response, the Planner performs a critical validation. It checks if the output is a valid list. To increase resilience, it also handles cases where the LLM might wrap the list in a dictionary (e.g., {"plan": [...]}) and extracts the list accordingly. If the structure is still incorrect, or if any other error occurs, the except block logs a detailed error message, including the raw LLM output for easier debugging, and raises the exception to halt the engine. 

### Executor
The Executor is the system’s on-site foreman: it runs each step, calls the right agent, and, most importantly, moves context forward so later steps can build on earlier results.

Before calling an agent, the Executor looks for placeholders in the input (things like $$...$$). These markers act as references to previous results, telling the system, “Use the output from step 1 here.” By resolving them, the Executor transforms the plan into a connected workflow. This is context chaining in action. The resolve_dependencies() helper drives this process. It scans the agent's required inputs for any $$...$$ placeholders.

The inner resolver (recursive cases) and execution contain the recursive part of the logic. If the value is not a string placeholder, it checks if it's a dictionary or a list. If it is, it recursively calls the resolve function on every item inside that dictionary or list. This allows the function to find placeholders nested deep within the input. The final return value handles any items that are neither placeholders nor nested structures.

Finally, the outer function executes this entire process by calling resolve(resolved_input):

```
# === 6.3. The Executor (Context Assembly and Execution) ===

def resolve_dependencies(input_params, state):
    """
    Helper function to replace 
 placeholders with actual data from the execution state.
    This implements Context Chaining.
    """
    # Use copy.deepcopy to ensure the original plan structure is not modified
    resolved_input = copy.deepcopy(input_params)

    # Recursive function to handle potential nested structures
    def resolve(value):
        if isinstance(value, str) and value.startswith("$$") and value.endswith("$$"):
            ref_key = value[2:-2]
            if ref_key in state:
                # Retrieve the actual data (string) from the previous step's output
                print(f"[Engine: Executor] Resolved dependency {ref_key}.")
                return state[ref_key]
            else:
                raise ValueError(f"Dependency Error: Reference {ref_key} not found in execution state.")
        elif isinstance(value, dict):
            return {k: resolve(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [resolve(v) for v in value]
        return value

    return resolve(resolved_input)
```

### Execution Tracer

With the Planner and Executor working in tandem, the Context Engine is functional, but not yet transparent. To close the loop, we need a way to observe what happens inside the system, to trace how each decision and action unfolds. The ExecutionTrace class, therefore, acts as the Context Engine’s flight recorder, quietly documenting every stage of reasoning from the initial goal to the final output.

```
#@title 6.The Context Engine (Planner, Executor, Tracer)
# -------------------------------------------------------------------------
# This is the core innovation of Chapter 4. It replaces the linear
# Orchestrator with a dynamic, LLM-driven planning and execution system.
# -------------------------------------------------------------------------

# === 6.1. The Tracer (Debugging Implementation) ===
class ExecutionTrace:
    """Logs the entire execution flow for debugging and analysis."""
    def __init__(self, goal):
        self.goal = goal
        self.plan = None
        self.steps = []
        self.status = "Initialized"
        self.final_output = None
        self.start_time = time.time()

    def log_plan(self, plan):
        self.plan = plan

    def log_step(self, step_num, agent, planned_input, mcp_output, resolved_input):
        """Logs the details of a single execution step."""
        self.steps.append({
            "step": step_num,
            "agent": agent,
             # The raw input definitions from the plan (including 
)
            "planned_input": planned_input,
            # Crucial for debugging: What exact context did the agent receive?
            "resolved_context": resolved_input,
            "output": mcp_output['content']
        })

    def finalize(self, status, final_output=None):
        self.status = status
        self.final_output = final_output
        self.duration = time.time() - self.start_time

    def display_trace(self):
        """Displays the trace in a readable format."""
        display(Markdown(f"### Execution Trace\n**Goal:** {self.goal}\n**Status:** {self.status} (Duration: {self.duration:.2f}s)"))
        if self.plan:
            # Display the raw plan JSON
            display(Markdown(f"#### Plan:\n```json\n{json.dumps(self.plan, indent=2)}\n```"))

        display(Markdown("#### Execution Steps:"))
        for step in self.steps:
            print(f"--- Step {step['step']}: {step['agent']} ---")
            print("  [Planned Input]:", step['planned_input'])
            # print("  [Resolved Context]:", textwrap.shorten(str(step['resolved_context']), width=150))
            print("  [Output Snippet]:", textwrap.shorten(str(step['output']), width=150))
            print("-" * 20)
```

#### Putting it all together

We now have all the building blocks in place: the Planner that thinks, the Executor that acts, and the Tracer that records every move. The final step is to connect them into a single control loop.

The context_engine() function is the system’s ignition switch. It brings everything to life by orchestrating the complete two-phase process: first, it plans the work, and then it works the plan. Let’s walk through it step by step.



```
def context_engine(goal):
    """
    The main entry point for the Context Engine. Manages Planning and Execution.
    """
    print(f"\n=== [Context Engine] Starting New Task ===\nGoal: {goal}\n")
    trace = ExecutionTrace(goal)
    registry = AGENT_TOOLKIT

    # Phase 1: Plan
    try:
        capabilities = registry.get_capabilities_description()
        plan = planner(goal, capabilities)
        trace.log_plan(plan)
    except Exception as e:
        trace.finalize("Failed during Planning")
        # Return the trace even in failure for debugging
        return None, trace

    # Phase 2: Execute
    # State stores the raw outputs (strings) of each step: { "STEP_X_OUTPUT": data_string }
    state = {}

    for step in plan:
        step_num = step.get("step")
        agent_name = step.get("agent")
        planned_input = step.get("input")

        print(f"\n[Engine: Executor] Starting Step {step_num}: {agent_name}")

        try:
            handler = registry.get_handler(agent_name)

            # Context Assembly: Resolve dependencies
            resolved_input = resolve_dependencies(planned_input, state)

            # Execute Agent via MCP
            # Create an MCP message with the RESOLVED input for the agent
            mcp_resolved_input = create_mcp_message("Engine", resolved_input)
            mcp_output = handler(mcp_resolved_input)

            # Update State and Log Trace
            output_data = mcp_output["content"]

            # Store the output data (the context itself)
            state[f"STEP_{step_num}_OUTPUT"] = output_data
            trace.log_step(step_num, agent_name, planned_input, mcp_output, resolved_input)
            print(f"[Engine: Executor] Step {step_num} completed.")

        except Exception as e:
            error_message = f"Execution failed at step {step_num} ({agent_name}): {e}"
            print(f"[Engine: Executor] ERROR: {error_message}")
            trace.finalize(f"Failed at Step {step_num}")
            # Return the trace for debugging the failure
            return None, trace

    # Finalization
    final_output = state.get(f"STEP_{len(plan)}_OUTPUT")
    trace.finalize("Success", final_output)
    print("\n=== [Context Engine] Task Complete ===")

    # Return the output of the final step AND the trace
    return final_output, trace
```

#### Running the engine

We’ve built each piece of the puzzle: the specialists, the registry, the Planner, the Executor, and the Tracer. After all this architectural work, it’s time to turn the key and hear the engine run. Let’s see what happens when the Context Engine is asked to tackle a creative goal from start to finish

```
print("******** Example 1: STANDARD WORKFLOW (Suspenseful Narrative) **********\n")
goal_1 = "Write a short, suspenseful scene for a children's story about the Apollo 11 moon landing, highlighting the danger."

# Run the Context Engine
# Ensure the Pinecone index is populated (from Ch3 notebook) for this to work.
result_1, trace_1 = context_engine(goal_1)

if result_1:
    print("\n******** FINAL OUTPUT 1 **********\n")
    display(Markdown(result_1))
    print("\n\n" + "="*50 + "\n\n")
    # Optional: Display the trace to see the engine's process
    # trace_1.display_trace()

```

