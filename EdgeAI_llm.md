[Browser-Based LLMs in Healthcare](https://dev.to/shieldstring/browser-based-llms-in-healthcare-2e72)

- Browser-based Large Language Models (LLMs) dissolve this tension by moving the inference engine off the server and directly into the user's browser, keeping sensitive medical data entirely on-device.

- Traditional healthcare AI follows a client-server model: the frontend collects data, ships it to a cloud API, and receives a response. Browser-based LLMs invert this entirely.

Patient Input (Symptoms / Record)
        ↓
  PII Scrubber (Transformers.js — Local NER)
        ↓
  Anonymized Text
        ↓
  LLM Inference (WebLLM + WebGPU)
        ↓
  Private Summary / Clinical Output
        ↑
  All processing stays inside the browser sandbox


The key enabling technologies are:

- WebGPU: A modern browser API that exposes the device's GPU to web applications, enabling tensor operations at near-native speed
- WebLLM (MLC AI): An in-browser inference engine that compiles quantized models (e.g., INT4) to WebGPU-optimized WASM bytecode github
- Transformers.js: A JavaScript port of HuggingFace Transformers that supports NER, classification, and embedding tasks on-device
- WebAssembly (WASM): Provides a portable, sandboxed execution runtime for compiled model weights in the browser


  Real-World Healthcare Use Cases
- 1. EMR De-identification and Anonymization
Electronic Medical Records (EMRs) are rich in PHI — names, dates, diagnoses, prescription details. Before sharing records for research or inter-departmental review, they must be de-identified. A browser-based pipeline using Transformers.js for Named Entity Recognition (NER) can strip PII from clinical notes locally, then pass the anonymized text to a WebLLM instance for summarization — all without the raw record ever leaving the browser.

- 2. Private Symptom Screening
A browser-based symptom screener allows patients to describe their symptoms in natural language and receive triage-level guidance — without their health disclosures being logged on any external server. This is especially significant for stigmatized conditions (mental health, HIV, substance use) where patients may withhold information if they suspect surveillance.

- 3. Clinical Note Generation
LLMs have shown strong performance in generating structured SOAP notes from free-form physician dictation. Running this process in-browser means a physician can dictate, receive a structured draft, review it, and commit only the final note to the EHR — with the intermediate AI processing completely local. pmc.ncbi.nlm.nih

- 4. Patient-Facing EHR Interpretation
Projects like LLMonFHIR demonstrate how LLMs can translate complex FHIR-formatted EHR data into patient-friendly natural language. A browser-based version of this would allow patients to query their own records conversationally, with full confidence that their medical history never passes through a third-party AI service. pmc.ncbi.nlm.nih

```
import * as webllm from "@mlc-ai/web-llm";

const engine = await webllm.CreateMLCEngine(
  "Llama-3-8B-Instruct-q4f16_1-MLC",
  {
    initProgressCallback: (report) => console.log(report.text),
  }
);

async function getMedicalSummary(anonymizedNote: string): Promise<string> {
  const messages = [
    {
      role: "system",
      content:
        "You are a clinical documentation assistant. " +
        "Summarize the following anonymized patient note in structured SOAP format. " +
        "Do not fabricate clinical details. Flag ambiguous sections for physician review.",
    },
    { role: "user", content: anonymizedNote },
  ];

  const response = await engine.chat.completions.create({ messages });
  return response.choices[0].message.content ?? "";
}
```
