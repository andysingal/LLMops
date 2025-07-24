Multi-Model Service is designed to co-host multiple models in one serving container, sharing GPU/CPU and memory across multiple models, and to load and unload models dynamically based on the incoming traffic. This can help you save significantly on costs and achieve the best price performance.

Multi-Model Service is an ideal solution when you need to serve a large number of models efficiently without loading them all into memory at once.

Instead of dedicating a separate container to each model, this approach has models share compute resources within a single serving instance.

Load the model only when a customer requests a prediction, and unload it when it’s inactive or when memory needs to be freed up for a new model. This significantly reduces infrastructure costs and improves resource utilization, making the model serving far more scalable.

The Model Server Inference Backend is designed to handle multiple types of models in a black-box manner. Regardless of the model algorithm and version, it can serve these models with an unified web prediction API. 

The Model Cache Management component has two responsibilities. First, it loads a given model from model storage into the Model Server Inference Backend. Second, it prevents the container resources from model overload by maintaining a Least Recently Used (LRU) cache to track all the modeled models, so it can unload the least-used models when the container’s resource utilization is high.

If memory and disk consumption is above a specified threshold (for example, 80%), the management component will find the least used model in its cache, unload it from the server backend, and remove the model from cache and disk.


### multi-model service tends to struggle in the following situations:

- When the models are too large to fit in one GPU. Either there is no room to share or lots of model unloading is required to make memory space available. This causes a lot of model loading overhead and cold-start latency for future models.

- When individual models have high traffic levels, which requires low-latency, always-loaded models. Single-model service is better in these cases.

- When the models have different security policies.

- When operational complexity is high. For instance, deployment, debugging, and monitoring are complicated due to the number of moving pieces in the system, such as model cache management, per-model routing and scaling, model compatibility, and dependency conflicts.
