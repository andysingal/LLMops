[ZenML](https://docs.zenml.io/user-guide/production-guide/understand-stacks.) introduced the concept of a stack, which allows you to run ZenML on multiple infrastructure options. A stack will enable you to connect ZenML to different cloud services, such as:

- An orchestrator(An orchestrator is a system that automates, schedules, and coordinates all your ML pipelines) and compute engine (for example, AWS SageMaker or Vertex AI)
- Remote storage (for instance, AWS S3 or Google Cloud Storage buckets)
- A container registry (for example, Docker Registry or AWS ECR)

Artifact: It is any file(s) produced during the machine learning lifecycle, such as datasets, trained models, checkpoints, or logs.



ZenML acts as a glue that brings all your infrastructure and tools together in one place through its stack feature, allowing you to quickly iterate through your development processes and easily monitor your entire ML system.


<strong>How does ZenML work as an orchestrator?</strong> 

It works with pipelines and steps. A pipeline is a high-level object that contains multiple steps. A function becomes a ZenML pipeline by being decorated with @pipeline, and a step when decorated with @step. This is a standard pattern when using orchestrators: you have a high-level function, often called a pipeline, that calls multiple units/steps/tasks.
```py
from zenml import pipeline
from steps.etl import crawl_links, get_or_create_user
@pipeline
def digital_data_etl(user_full_name: str, links: list[str]) -> None:
    user = get_or_create_user(user_full_name)
    crawl_links(user=user, links=links)
```

You can run the pipeline with the following CLI command: ```poetry poe run-digital-data-etl```. To visualize the pipeline run, you can go to your ZenML dashboard (at http://127.0.0.1:8237/)

 In the code snippet below, we defined the ```get_or_create_user()``` step, which works just like a normal Python function but is decorated with @step
 ```py
from loguru import logger
from typing_extensions import Annotated
from zenml import get_step_context, step
from llm_engineering.application import utils
from llm_engineering.domain.documents import UserDocument
@step
def get_or_create_user(user_full_name: str) -> Annotated[UserDocument, "user"]:
    logger.info(f"Getting or creating user: {user_full_name}")
    first_name, last_name = utils.split_user_full_name(user_full_name)
    user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)
    return user
```
The modularity of your code makes it easy to decorate your functions with ```@step``` and then glue multiple steps together within a main function decorated with ```@pipeline```.



