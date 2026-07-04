[Building Reliable Agentic AI Systems](https://martinfowler.com/articles/reliable-llm-bayer.html)

-  key engineering decisions through the lens of context engineering—how information was shaped and routed between specialized agents—and harness engineering—how orchestration, recovery, and observability were built around the models to maintain control and reliability
- Like a horse harness takes raw power and lets it pull a cart, an AI harness takes raw intelligence and lets it do real work --- Ethan Mollick
- It gives the model: 1. Tools(Web search, code execution, file access...) 2. Actions (browse sites, send messages, run commands) 3. Multi-step task orchestration 4. Instructions on how to approach problems

- User Request: the process begins when a user submits a request through the Conversational UI which is built with React.
- Orchestration: the user's request is routed to a LangGraph-based orchestration layer in the backend. This workflow engine coordinates a multi-stage process that progresses through clarifying user intent, thinking and planning, conducting research (using RAG and Text-to-SQL), validating data completion, and finally generating a response through the Writer agent. The workflow includes deliberate pause points and feedback loops to ensure data completeness before proceeding. (We explore the details of this agentic workflow in a dedicated section later.)
- Data Retrieval and State Management: the Researcher agents interact with a comprehensive and distributed data ecosystem:
- Vector representations of all study reports are stored in OpenSearch, forming the core knowledge base for information retrieval.
- Curated structured data, resulting from various ETL and harmonization processes, is accessed via Athena.
- The state of the agent's execution is meticulously tracked. After each logical step (a LangGraph node execution), the corresponding state is persisted in PostgreSQL using a LangGraph checkpointer.
- Broader application-level state is managed in DynamoDB.

Observability and Evaluation: the entire system is monitored for performance and reliability:
- General system health and metrics are tracked using Cloudwatch.
- Langfuse serves as the primary observability tool, providing detailed traces of all production traffic. This allows for in-depth debugging of issues. Furthermore, evaluation datasets are stored and managed within Langfuse, making it easier to analyze performance scores and diagnose specific failures. The evaluation is done using RAGAS evaluation framework. The live traffic evaluation is done on a daily basis while the dataset evaluation is done whenever significant changes are made to the core workflow, prompts, or underlying models.

- Final Response: once the agents have processed the request and generated a satisfactory response, it is sent back to the Conversational UI to be presented to the user.

### Think & Plan: Process Reflection

In multi-step agentic workflows, particularly those involving many sequential actions, process reflection is essential. Consider a scenario where the system needs to execute 50 steps to complete a complex task. At each juncture, the system must ask: Am I taking these steps in the right manner? Am I making the progress I'm supposed to make? Is the current trajectory leading toward the user's goal? The Think & Plan step provides this metacognitive capability, allowing the system to reflect on its own workflow and adjust its strategy accordingly.

For instance, the system might first query structured metadata to identify relevant studies, then use those study IDs to retrieve detailed information from unstructured reports, and finally synthesize the findings. Without a dedicated space for process reflection, the system would attempt to execute these steps linearly without evaluating whether each step is bringing it closer to the goal. With the thinking step in place, the system can pause, assess its progress in the workflow, and intelligently plan the subsequent tool calls needed to complete the user's request.

 the top‑level Researcher Agent is designed to act as a coordinator rather than a single all‑knowing component. Given the clarified user intent and any explicit domain selection from the UI, it will route the query to the appropriate domain sub‑agent, which can then decide how to combine RAG and Text‑to‑SQL within its own boundary. 

[Don't Train the Model,Evolve the Harness](https://huggingface.co/spaces/joelniklaus/harness-optimization#introduction)


 
