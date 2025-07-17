 Model serving refers to deploying an ML model in a production environment, where it can process new data and generate predictions

 Model serving can happen locally (on-device), in-cluster (on-premises), or remotely (on-cloud), depending on the business requirements and infrastructure constraints.

 Here are three examples, one for each serving scenario:

1.  Warehouse robot (on-device): A real-time object detection model (such as YOLO) is deployed on a robot’s onboard computer (say, a Raspberry Pi with a Coral TPU). This lets the robot process visual input and make autonomous decisions instantly.

2. Document search (on-premises): To build a semantic search index on internal company data, a language model (likeSentence-BERT) is served within the company’s computing cluster. This setup generates dense vector embeddings for documents while ensuring data security and compliance by avoiding large-scale data transfers.

3. Customer support chatbot (on-cloud): When a customer submits a query, the chatbot sends it, along with relevant documents, to a remote LLM hosted or provided by a vendor, such as openAI, Sagemaker


Note: In the model-serving context, ML and DevOps engineers typically focus less on models’ internal details—such as their architecture, training methods, and file formats—and instead treat models as black boxes. This is because modern model-serving frameworks like vLLM and TensorRT-LLM handle the complexities of model execution for us, providing a high-level abstraction that makes running model predictions simpler and more efficient.

In model serving, we focus more on the following:

- Deployment: Choosing the right hardware and making the model available from the training pipeline (or from open source options) to consume input data and return predictions.

- Scalability and Availability: The ability to handle a few thousand to millions of requests efficiently while ensuring a consistent customer experience.

- Latency: Delivering predictions quickly–in milliseconds, for real-time use cases.

- Monitoring: Tracking model performance, data drift, and system health.

- Versioning: Managing model updates and rollbacks without disrupting clients.

- Security: Sensitive data must be protected, and access to the model should be controlled.

- Cost to Serve: The most decisive factor of them all. We use cost-to-serve as a key factor to evaluate different serving approaches and trade-offs.

Model serving is a highly practical, engineering-focused field. Unlike AI research and model training, it does not require a deep understanding of ML algorithms or an academic background in AI. Instead, it emphasizes deploying and integrating models into real-world applications using existing tools and frameworks.
