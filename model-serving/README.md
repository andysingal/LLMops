 Model serving refers to deploying an ML model in a production environment, where it can process new data and generate predictions

 Model serving can happen locally (on-device), in-cluster (on-premises), or remotely (on-cloud), depending on the business requirements and infrastructure constraints.

 Here are three examples, one for each serving scenario:

1.  Warehouse robot (on-device): A real-time object detection model (such as YOLO) is deployed on a robot’s onboard computer (say, a Raspberry Pi with a Coral TPU). This lets the robot process visual input and make autonomous decisions instantly.

2. Document search (on-premises): To build a semantic search index on internal company data, a language model (likeSentence-BERT) is served within the company’s computing cluster. This setup generates dense vector embeddings for documents while ensuring data security and compliance by avoiding large-scale data transfers.

3. Customer support chatbot (on-cloud): When a customer submits a query, the chatbot sends it, along with relevant documents, to a remote LLM hosted or provided by a vendor, such as openAI, Sagemaker

