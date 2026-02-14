Context engineering is the art and science of controlling and directing the informational world that a Large Language Model (LLM) has learned.



<img width="474" height="607" alt="Screenshot 2026-02-13 at 2 25 49 PM" src="https://github.com/user-attachments/assets/999dfac2-6d18-41fa-9278-83552e49e300" />

- Level 1: The basic prompt (zero context). This is a simple instruction with no background. The AI guesses based on training data, producing generic or clichéd outputs.
<img width="338" height="601" alt="Screenshot 2026-02-13 at 2 28 36 PM" src="https://github.com/user-attachments/assets/5ba6f48f-e466-47e3-9770-5d53794488ff" />
- Level 2: The better context (linear context). This is a small step forward. Adding a linear thread improves factual accuracy compared to zero context, but the model still lacks style, purpose, or direction.
<img width="460" height="592" alt="Screenshot 2026-02-13 at 2 30 28 PM" src="https://github.com/user-attachments/assets/024affe4-1eea-4e24-b674-e78a4f247969" />
- Level 3: The good context (goal-oriented context). This would be the first true context level. By giving the model a clear goal, its responses become intentional and aligned. This is the first acceptable milestone in context engineering.
<img width="339" height="612" alt="Screenshot 2026-02-13 at 2 31 51 PM" src="https://github.com/user-attachments/assets/b770b6d9-709f-4673-902f-38c098e2adff" />

- Level 4: The advanced context (role-based context). This is more structured than goal-only prompts. By assigning explicit roles, the model can follow conflict and motivation, producing narratively intelligent responses.
<img width="366" height="593" alt="Screenshot 2026-02-13 at 2 35 04 PM" src="https://github.com/user-attachments/assets/23bc4a3a-7590-4a24-983f-163ab8c9c794" />

- Level 5: The semantic blueprint. This is the ultimate engineered context. A precise,unambiguous plan using semantic roles transforms creativity into a reliable, repeatable engineering process.
```
TASK: Generate a single, suspenseful sentence.
---
SEMANTIC BLUEPRINT:
{
  "scene_goal": "Increase tension by showing defiance",
  "participants": [
    { "name": "Onyx", "role": "Agent", "description": "black cat" },
    { "name": "Red Ball", "role": "Patient", "description": "mysterious" },
    { "name": "Grandfather Clock", "role": "Source_of_Threat", "description": "ancient, looming" }
  ],
"action_to_complete": {
            "predicate": "play with",
 "agent": "Onyx",
 "patient": "Red Ball"
  }
}
---
SENTENCE TO COMPLETE: "He then played with the..."
```

But how do we construct such a blueprint from the linear, often ambiguous flow of human language? To do so, we must stop seeing sentences as strings of words and start viewing them as structures of meaning.

## Definitions:
- Context Chaining: Context chaining (or prompt chaining) is an AI engineering technique that breaks complex tasks into smaller, sequential steps, where the output of one prompt becomes the input for the next(Insights --> decision ---> professional action)
- Semantic Role Labeling: A linguistic technique that reveals who did what to whom, when, and why.

A context engineer, using SRL, sees more: a stemma, or graph, that maps each word to its semantic role. The central action is “pitched”, while every other component is assigned a role in relation to that action.

By labeling these roles, we will do the following:

- Reconstruct the multidimensional semantic structure of an otherwise linear string of words
- Define a semantic blueprint that an LLM can follow, as demonstrated in the Level 5 example earlier

<img width="329" height="571" alt="Screenshot 2026-02-13 at 3 01 23 PM" src="https://github.com/user-attachments/assets/9a40e11c-8d53-4336-8736-7ec047d73b13" />

- User Input: The journey begins when you call the main function, visualize_srl(). Here, you provide the building blocks of the sentence, such as its verb (predicate), the agent (the entity performing the action), the patient (the entity receiving or affected by the action), and other semantic roles represented as textual arguments.
- Data Structuring: The main function organizes these components into a Python dictionary. Each entry is assigned the proper SRL label, so what began as a loose list of words becomes a structured map of roles.
- The Plotting Engine: Once the dictionary is ready, it is passed to an internal helper function, _plot_stemma. This function does one thing only: draw.
- Canvas Setup: The plotting engine creates a blank canvas using Matplotlib, preparing the stage for the diagram.
- Dynamic Positioning: The function calculates where to place each role node so the layout remains clear and balanced, regardless of how many components are included.
- Drawing the Stemma (Graph): The engine then draws the core verb as the root node, adds each role as a child node, and connects them with labeled arrows. What was once a linear sentence is now a visual map of meaning.
- Final Display: Finally, the function adds a title and displays the completed semantic blueprint.

<img width="516" height="252" alt="Screenshot 2026-02-13 at 3 20 27 PM" src="https://github.com/user-attachments/assets/3854e10f-7777-462f-8c17-324259447edc" />


## Engineering a meeting analysis use case:

- Establishing the scope
- Conducting the investigation
- Determining the action

This meeting analysis demonstrates a powerful technique called context chaining, where we guide an LLM through a multi-step analysis. Instead of one large, complex prompt, we use a series of simpler, focused prompts, where the output of one step becomes the input for the next. This creates a highly controlled and logical workflow.

We use a context chaining process because an LLM, despite its power, has no true memory or long-term focus. Giving an LLM a single, massive prompt with a complex, multi-step task is akin to giving a brilliant but forgetful assistant a lengthy list of verbal instructions and hoping for the best. The model will often lose track of the primary goal, get bogged down in irrelevant details, and produce a muddled, unfocused result.

Context chaining solves this problem by transforming a complex task into a controlled, step-by-step dialogue. Each step has a single, clear purpose, and its output becomes the clean, focused input for the next step. This method gives you, the context engineer, three critical advantages:

- Precision and control: You can guide the AI's thought process at each stage, ensuring the analysis stays on track
- Clarity and debugging: If one step produces a poor result, you know exactly which prompt to fix, rather than trying to debug a single, monolithic instruction
- Building on insight: It creates a narrative flow, allowing the AI to build upon the refined insights from the previous step, leading to a far more sophisticated and coherent final outcome

<img width="520" height="448" alt="Screenshot 2026-02-13 at 3 34 38 PM" src="https://github.com/user-attachments/assets/0f593454-d0f3-428a-9c3a-db172e95b29b" />


<img width="485" height="615" alt="Screenshot 2026-02-13 at 3 35 27 PM" src="https://github.com/user-attachments/assets/5c4f3fbe-1073-4235-9acf-aa4cb1e6d462" />


```
#### Let's now translate this flowchart plan into actual code and run it step by step:
!pip install openai

### This workflow uses Google Colab Secrets to store the OpenAI API key. Load the key, set the environment variable, and initialize the client:

# Cell 2: Imports and API Key Setup
# We will use the OpenAI library to interact with the LLM and Google Colab's
# secret manager to securely access your API key.

import os
from openai import OpenAI
from google.colab import userdata

# Load the API key from Colab secrets, set the env var, then init the client
try:
    api_key = userdata.get("API_KEY")
    if not api_key:
        raise userdata.SecretNotFoundError("API_KEY not found.")

    # Set environment variable for downstream tools/libraries
    os.environ["OPENAI_API_KEY"] = api_key

    # Create client (will read from OPENAI_API_KEY)
    client = OpenAI()
    print("OpenAI API key loaded and environment variable set successfully.")

except userdata.SecretNotFoundError:
    print('Secret "API_KEY" not found.')
    print('Please add your OpenAI API key to the Colab Secrets Manager.')
except Exception as e:
    print(f"An error occurred while loading the API key: {e}")

### Add the meeting transcript as a multi-line string. This will be the input for the chained steps that follow:
# Cell 3: The Full Meeting Transcript
meeting_transcript = """
        Tom: Morning all. Coffee is still kicking in.
        Sarah: Morning, Tom. Right, let's jump in. Project Phoenix timeline. Tom, you said the backend components are on track?
        Tom: Mostly. We hit a small snag with the payment gateway integration. It's... more complex than the docs suggested. We might need another three days.
        Maria: Three days? Tom, that's going to push the final testing phase right up against the launch deadline. We don't have that buffer.
        Sarah: I agree with Maria. What's the alternative, Tom?
        Tom: I suppose I could work over the weekend to catch up. I'd rather not, but I can see the bind we're in.
        Sarah: Appreciate that, Tom. Let's tentatively agree on that. Maria, what about the front-end?
        Maria: We're good. In fact, we're a bit ahead. We have some extra bandwidth.
        Sarah: Excellent. Okay, one last thing. The marketing team wants to do a big social media push on launch day. Thoughts?
        Tom: Seems standard.
        Maria: I think that's a mistake. A big push on day one will swamp our servers if there are any initial bugs. We should do a soft launch, invite-only for the first week, and then do the big push. More controlled.
        Sarah: That's a very good point, Maria. A much safer strategy. Let's go with that. Okay, great meeting. I'll send out a summary.
        Tom: Sounds good. Now, more coffee.
        """

```
<strong><h2>Layer 1: Establishing the scope (the “what”)</h2></strong>

<h3>Tell the model exactly what to extract and what to ignore. The goal is to separate substantive content (decisions, updates, problems, proposals) from conversational noise (greetings, small talk).</h3>

```
# Cell 4: g2 - Isolating Content from Noise
prompt_g2 = f"""
        Analyze the following meeting transcript. Your task is to isolate the substantive content from the conversational noise.
        - Substantive content includes: decisions made, project updates, problems raised, and strategic suggestions.
        - Noise includes: greetings, pleasantries, and off-topic remarks (like coffee).
        Return ONLY the substantive content.

        Transcript:
        ---
        {meeting_transcript}
        ---
        """
```
<h3>Now we activate OpenAI to isolate the substantive content:</h3>

```
from openai import OpenAI
try:
    client = OpenAI()

    response_g2 = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "user", "content": prompt_g2}
        ]
    )

    substantive_content = response_g2.choices[0].message.content
    print("--- SUBSTANTIVE CONTENT ---")
    print(substantive_content)

except Exception as e:
    print(f"An error occurred: {e}")
```
<h3>The output displays the substantive content:</h3>

```md
--- SUBSTANTIVE CONTENT ---
- Project Phoenix timeline: Backend mostly on track, but payment gateway integration is more complex than expected; needs an additional three days.
- Impact: Extra three days would push final testing up against the launch deadline, reducing buffer.
- Mitigation decision: Tom will work over the weekend to catch up (tentatively agreed).
- Front-end status: Ahead of schedule with extra bandwidth.
- Marketing/launch strategy: Initial plan for a big social media push on launch day flagged as risky (potential server load with early bugs). Decision: Use a soft launch (invite-only) for the first week, then execute the big push.
```

 <h3>Next, we simulate a retrieval-augmented generation (RAG) context by comparing the new meeting with a summary of the previous one. This narrows the focus to what’s new, showing the importance of historical context:</h3>   

 ```
# Cell 5: g3 - Identifying NEW Information (Simulated RAG)
previous_summary = "In our last meeting, we finalized the goals for Project Phoenix and assigned backend work to Tom and front-end to Maria."

prompt_g3 = f"""
Context: The summary of our last meeting was: "{previous_summary}"

Task: Analyze the following substantive content from our new meeting. Identify and summarize ONLY the new developments, problems, or decisions that have occurred since the last meeting.

New Meeting Content:
---
{substantive_content}
---
"""
```

```
from openai import OpenAI
from google.colab import userdata

# Your chat completion request
try:
    response_g3 = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt_g3}]
    )
    new_developments = response_g3.choices[0].message.content
    print("--- NEW DEVELOPMENTS SINCE LAST MEETING ---")
    print(new_developments)
except Exception as e:
    print(f"An error occurred: {e}")
```

```
--- NEW DEVELOPMENTS SINCE LAST MEETING ---
- Backend issue: Payment gateway integration is more complex than expected; needs an additional three days.
- Schedule impact: The extra three days compress final testing, pushing it up against the launch deadline and reducing buffer.
- Mitigation decision: Tentative agreement that Tom will work over the weekend to catch up.
- Front-end status: Ahead of schedule with extra bandwidth.
- Launch/marketing decision: Shift from a big day-one social push to a one-week invite-only soft launch, followed by the major push.

```

<strong><h2>Layer 2: Conducting the investigation (the “how”)</h2></strong>
<h3>Beyond explicit facts, every meeting carries subtext: hesitations, tensions, and moods. This step asks the AI to analyze the underlying dynamics:</h3>

```
# Cell 6: g4 - Uncovering Implicit Threads
prompt_g4 = f"""
Task: Analyze the following meeting content for implicit social dynamics and unstated feelings. Go beyond the literal words.
- Did anyone seem hesitant or reluctant despite agreeing to something?
- Were there any underlying disagreements or tensions?
- What was the overall mood?

Meeting Content:
---
{substantive_content}
---
"""
```

<h3>We now run the prompt to explore the implicit dynamics of the meeting beyond the literal words:</h3>

```
try:
    response_g4 = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt_g4}]
    )
    implicit_threads = response_g4.choices[0].message.content
    print("--- IMPLICIT THREADS AND DYNAMICS ---")
    print(implicit_threads)
except Exception as e:
    print(f"An error occurred: {e}")
```

<h3>Output</h3>

```
--- IMPLICIT THREADS AND DYNAMICS ---
Here's what seems to be happening beneath the surface:

Hesitation/reluctance despite agreement
- Tom's "tentative" agreement to work over the weekend reads as reluctant. It suggests he felt pressure to volunteer rather than genuine willingness.
- Marketing likely agreed to the soft launch with some reluctance; shifting from a big day-one push to invite-only implies a concession to engineering risk.

Underlying disagreements or tensions
- Pace vs quality: Engineering wants stability and buffer; marketing originally aimed for impact. The soft launch is a compromise, but the differing risk appetites remain.
- Workload equity: Backend is behind while frontend has "extra bandwidth." The decision to have Tom work the weekend (vs redistributing tasks) hints at siloing or a norm of individual heroics, which can breed quiet resentment.
- Testing squeeze: Pushing testing against the deadline implies QA will be under pressure, potentially creating friction if bugs slip through or late changes occur.
- Estimation confidence: The payment gateway being "more complex than expected" may subtly challenge earlier estimates, inviting unspoken doubt about planning or vendor integration assumptions.

Overall mood
- Sober, pragmatic, and slightly tense. The group is solution-oriented and collaborative, but there's a sense of urgency and strain, with relief at having a plan tempered by concerns about workload, risk, and reduced buffer.
```

This is where context chaining shifts from recording what happened to interpreting why it matters. The result feels less like a raw transcript and more like an analyst’s commentary, giving us insights into team dynamics that would otherwise remain unstated.

<h3>Next, we prompt the AI to be creative and solve a problem by synthesizing different ideas from the meeting, demonstrating its thinking power:</h3>

```
# Cell 7: g5 - Generating a Novel Solution
prompt_g5 = f"""
Context: In the meeting, Maria suggested a 'soft launch' to avoid server strain, and also mentioned her team has 'extra bandwidth'.
Tom is facing a 3-day delay on the backend.

Task: Propose a novel, actionable idea that uses Maria's team's extra bandwidth to help mitigate Tom's 3-day delay. Combine these two separate pieces of information into a single solution.
"""
try:
    response_g5 = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt_g5}]
    )
    novel_solution = response_g5.choices[0].message.content
    print("--- NOVEL SOLUTION PROPOSED BY AI ---")
    print(novel_solution)
except Exception as e:
    print(f"An error occurred: {e}")
```

```md
--- NOVEL SOLUTION PROPOSED BY AI ---
Idea: Soft launch behind a temporary "Edge Bridge" that Maria's team builds to buffer reads/writes until Tom's backend is ready.

What Maria's team does (uses their extra bandwidth)
- Stand up a thin serverless/API facade that matches the real API contracts (e.g., API Gateway/Lambda + SQS/DynamoDB or Cloudflare Workers + Durable Objects).
- Reads: Serve from a prewarmed cache or static snapshots (stale-while-revalidate). Update snapshots hourly via a lightweight data export from staging or existing endpoints.
- Writes: Capture requests into a durable queue with idempotency keys; return immediate "queued" success to the client and show "syncing" UI. When Tom's backend is live, a replay worker drains the queue and applies changes.
- Add feature flags/traffic gating (e.g., LaunchDarkly) to limit the soft launch cohort and throttle requests to avoid server strain.

How this mitigates the 3-day delay
- The product can soft-launch to a small cohort without waiting for the backend; users get read access and buffered writes.
- When Tom's backend is ready, flip routing to the real backend and drain the queue to reconcile data.

Action plan and timeline
- Day 0 (today): Identify minimal critical endpoints for the soft launch. Classify by read vs write. Define API contracts and idempotency rules. Set success/error thresholds and a kill switch.
- Day 1: Maria's team builds the Edge Bridge, cache, and write queue; implement basic observability and encryption-at-rest for any PII in the queue. Front-end adds "syncing" UI states and feature flags.
- Day 2: QA with mocked data, then with a tiny internal cohort. Prewarm caches. Set traffic cap (e.g., 5–10% of target users).
- Day 3: Soft launch goes live on the Edge Bridge. When Tom's backend unlocks, switch routing gradually, start replay worker, monitor for conflicts, then retire the bridge.

Risk controls
- Data consistency: Use idempotency keys and a simple conflict policy (latest-write-wins or version checks).
- Rollback: Feature flag to disable writes or pause replay if error rate exceeds threshold.
- Privacy: Encrypt queued payloads; limit PII scope.

Owners
- Maria's team: Edge Bridge, caching, queue/replay, monitoring.
- Tom's team: Final backend endpoints, schema, and replay acceptance hooks.
- Front-end: Feature-flag routing and "queued/syncing" UX.

This combines Maria's extra bandwidth with a controlled soft launch to keep momentum while absorbing Tom's 3-day backend delay.
The output shows how an LLM can function as a creative collaborator, proposing
```

<h2>Layer 3: Determining the action (the “what next”</h2>

The next step is to compile everything into a structured, final summary.

This serves two purposes:

It forces clarity since every item is reduced to topic, outcome, and owner.
It makes information reusable. Whether dropped into an email, report, or dashboard, the summary is clean and immediately actionable.

```
# Cell 8: g6 - Creating the Final, Structured Summary
prompt_g6 = f"""
Task: Create a final, concise summary of the meeting in a markdown table.
Use the following information to construct the table.

- New Developments: {new_developments}

The table should have three columns: "Topic", "Decision/Outcome", and "Owner".
"""
try:
    response_g6 = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt_g6}]
    )
    final_summary_table = response_g6.choices[0].message.content
    print("--- FINAL MEETING SUMMARY TABLE ---")
    print(final_summary_table)
except Exception as e:
    print(f"An error occurred: {e}")
```

```
--- FINAL MEETING SUMMARY TABLE ---
| Topic | Decision/Outcome | Owner |
|---|---|---|
| Backend payment gateway integration | More complex than expected; requires an additional three days | Backend Team |
| Schedule impact | Extra three days compress final testing, reducing buffer before launch | Project Manager |
| Mitigation | Tentative plan: Tom will work over the weekend to catch up | Tom |
| Front-end status | Ahead of schedule with extra bandwidth available | Front-end Team |
| Launch/marketing plan | Shift to a one-week invite-only soft launch, then major day-one push | Marketing + Product |
```

- The final step in context chaining is to close the loop from insight to action: turning the structured analysis into a professional follow-up email:

```
# Cell 9: g7 - Drafting the Follow-Up Action
prompt_g7 = f"""
Task: Based on the following summary table, draft a polite and professional follow-up email to the team (Sarah, Tom, Maria).
The email should clearly state the decisions made and the action items for each person.

Summary Table:
---
{final_summary_table}
---
"""
```

```
try:
    response_g7 = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt_g7}]
    )
    follow_up_email = response_g7.choices[0].message.content
    print("--- DRAFT FOLLOW-UP EMAIL ---")
    print(follow_up_email)
except Exception as e:
    print(f"An error occurred: {e}")
```

```
--- DRAFT FOLLOW-UP EMAIL ---
Subject: Follow-up: Decisions and next steps from today's sync

Hi Sarah, Tom, and Maria,

Thanks for the productive discussion earlier. Here's a quick recap of decisions and the action items for each of us.

Decisions
- Backend payment gateway integration is more complex than expected and will require an additional three days.
- This pushes the schedule by three days and compresses the final testing window, reducing our pre-launch buffer.
- Mitigation: Tom will work over the weekend to help us catch up.
- Front-end is ahead of schedule and has extra bandwidth to support.
- Launch/marketing plan will shift to a one-week invite-only soft launch, followed by the larger day-one push.

Action items
- Tom:
  - Confirm weekend availability and share a brief plan (key milestones, dependencies, and any risks).
  - Proceed with the gateway integration and coordinate early integration testing with Front-end and QA.
  - Provide short daily progress updates and flag blockers immediately.

- Sarah:
  - Update the project timeline to reflect the three-day shift and the compressed QA window.
  - Coordinate with QA on a risk-based test plan that fits the shortened testing period.
  - Align with Marketing/Product on the invite-only soft launch scope, success metrics, and comms; circulate the plan to the team.

- Maria:
  - Reallocate Front-end bandwidth to support the backend integration (payment UI hooks, error handling, instrumentation).
  - Partner with Tom on mocks/stubs as needed to unblock early integration and QA.
  - Ensure front-end readiness for the soft launch (feature flags/toggles, tracking) and share any gaps.

Please reply to confirm your action items and note any constraints or support you need. I'm happy to set up a brief daily check-in while we work through this; propose a time if you have a preference.

Thanks all, and appreciate the quick coordination.

Best,
[Your Name]
```
This is the moment where the LLM stops being a “note-taker” and becomes a creative partner, as we mentioned at the start of this chapter. In this use case, we didn’t just get a summary. We witnessed how to think with the AI as a partner. The human remains at the center of the process and can create templates of context chaining for meetings, email processing, reporting, and anything you can imagine. Used well, context chaining can elevate the way teams, companies, and clients operate.

## Reference:
- [Agentic AI and Security](https://martinfowler.com/articles/agentic-ai-security.html)

<img width="573" height="666" alt="Screenshot 2026-02-14 at 8 50 28 AM" src="https://github.com/user-attachments/assets/4bc8fc32-1239-4f86-9528-15fbdfba6bd6" />



