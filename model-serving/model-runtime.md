- A model wrapper is a component implemented by the application developers to provide the model inference interfaces (functions) for the application logic to execute the model. The model wrapper encapsulates the details of how to interact with the model runtime, such as preprocessing the input data to model input, load the model into the model runtime, execute the model from the model runtime, and postprocess the output.

- A model runtime is a specialized software framework designed to execute ML models efficiently on different hardware platforms. It serves as the intermediary layer between the trained model and the device’s hardware, optimizing the inference process to maximize speed, efficiency, and resource utilization.

- The model runtime plays a crucial role in on-device AI by abstracting the complexities of model execution across different hardware (like smartphones, drones, and robots) and operating systems (iOS, Android, Linux). It also provides hardware-specific optimizations and acceleration techniques to improve inference performance.

- For example, the model runtime can leverage specialized hardware (like CPUs, GPUs, NPUs, and TPUs) for efficient inference. It also supports delegates (such as GPU Delegate, NNAPI for Android, and Core ML for iOS) to optimize performance.

- A well-designed model runtime allows developers to focus on building application features rather than worrying about hardware compatibility or model execution details. As of this writing, some of the most popular model runtimes include TensorFlow Lite (TFLite), ONNX Runtime (ORT) and Core ML.

- As AI app developers, we use model runtimes to execute models efficiently and encapsulate model-specific execution logic into a reusable module often called a model wrapper. This wrapper abstracts low-level details, making it easier to integrate, update, and optimize models within applications.

- A model wrapper is a component implemented by the application developers to provide the model inference interfaces (functions) for the application logic to execute the model. The model wrapper encapsulates the details of how to interact with the model runtime, such as preprocessing the input data to model input, load the model into the model runtime, execute the model from the model runtime, and postprocess the output.

- In the workflow shown in Figure 1-6 (a), the application logic first asks the model wrapper to execute a model with given data. The model wrapper takes care of data conversion and calls the model runtime to execute the model. The model runtime then handles the execution using the local hardware.
