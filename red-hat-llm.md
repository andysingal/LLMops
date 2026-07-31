[Combining KServe and llm-d for optimized generative AI inference](https://developers.redhat.com/articles/2026/04/21/kserve-llm-d-optimized-gen-ai-inference#)

Platform engineering leaders require more than model deployment capabilities. They need a Kubernetes-native infrastructure that supports efficient GPU utilization and intelligent request routing. This foundation also enables distributed inference patterns, cost-aware autoscaling, and production-grade governance.

KServe determines where the request should go. If no pods are running, it triggers scale-from-zero. If traffic increases, it scales horizontally based on real-time demand. Then, it routes the request through the appropriate revision of the service, whether that's a stable deployment or a canary rollout receiving partial traffic.


[Progress tracking in Red Hat OpenShift AI](https://www.redhat.com/en/blog/make-every-gpu-hour-count-progress-tracking-red-hat-openshift-ai?channel=/en/blog/channel/red-hat-ai)

Red Hat OpenShift AI now includes production-ready progress tracking for distributed training jobs, built into Kubeflow Trainer v2 and generally available beginning with Red Hat OpenShift AI 3.4. You can see what's happening while it's still happening—and act before it's too late.

- Dashboard visualization: Real-time progress metrics are visible directly in the Red Hat OpenShift AI dashboard. At a glance, you can see progress percentage, current step and total steps, current epoch, estimated time remaining, training loss, and evaluation metrics for your TrainJobs. No separate tool, no additional setup.
- SDK integration: The same progress data is available programmatically through the Kubeflow SDK. This enables teams to build automated pipelines that react to training progress—triggering early stopping, sending notifications, or reallocating resources based on real-time metrics.
- Multi-framework consistency: Progress tracking works the same way whether you're using PyTorch DDP, FSDP, DeepSpeed, or JAX. It also supports custom training code through the CustomTrainer API. This provides a single unified experience across frameworks.
