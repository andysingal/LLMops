1. Pre-training data - What’s it trained on? As the old computer science adage ‘Garbage In, Garbage Out’ comes back to bite us, we will explore popular pre-training datasets and dig into the various pre-processing steps taken to ensure high-quality data is fed to the model. We will also showcase some tools that allow us to probe these datasets and understand how pre-training data composition impacts downstream tasks.

2. Vocabulary and tokenizer - What’s it trained over? In order to build a model over a language, we have to first determine the vocabulary of the language we are modeling, and rules to break down a stream of text into the right vocabulary units (tokenization). Linguistically, humans process language in terms of meaning-bearing words and sentences. Language models process language in terms of tokens. We will explore the downstream impact when there is a mismatch between the two.

3. Learning objective - What is it being trained to do? By pre-training a language model, we aim to imbibe the language model with general skills in syntax, semantics, reasoning and so on, that will hopefully enable it to reliably solve any task you throw at it even if it was not specifically trained on it. We will discuss the various tasks (learning objectives) that pre-trained models are trained on. You might wonder if LLMs are better suited to solving downstream tasks that are similar to the tasks the pre-trained model has been trained to solve. We will test this assumption and discuss the impact various learning objectives have on task performance.

4. Architecture - What’s its internal structure? Most modern language models are based on the Transformer architecture. We will discuss the various architectural backbones- specifically encoder-only models, encoder-decoder models, and decoder-only models, and the rationale used by organizations training LLMs for their choice of architecture type.


<img width="635" alt="Screenshot 2024-04-18 at 7 16 06 PM" src="https://github.com/andysingal/LLMops/assets/20493493/82cf7456-441c-4256-b81f-a781cdee7b20">

The language models trained using the process described in this chapter and the next are called base models. Lately, model providers have been augmenting the base model by tuning it on much smaller datasets in order to steer them towards being more aligned with human needs and preferences. Some popular tuning modes are:

1. Supervised instruction fine-tuning, so that the model is better at following human instructions.

2. RLHF (Reinforcement Learning by Human Feedback), so that the model is better aligned with human preferences.

3. Domain-adaptive or task-adaptive continued pre-training, so that the model is better attuned to specific domains and tasks.

to name a few. Based on the specific augmentation carried out, the resulting models are called instruct models, chat models and so on.

<img width="840" alt="Screenshot 2024-04-18 at 7 57 23 PM" src="https://github.com/andysingal/LLMops/assets/20493493/8bb61f91-c8fb-4dcc-8cda-4f0f0ee8edf5">
