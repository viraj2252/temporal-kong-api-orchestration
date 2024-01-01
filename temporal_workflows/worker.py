import asyncio
import time
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import MyWorkflow, activity1, activity2


async def run_worker():
    client = await Client.connect("host.docker.internal:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client, task_queue="hello-task-queue", workflows=[MyWorkflow], activities=[activity1, activity2]
    )
    await worker.run()


if __name__ == "__main__":
    time.sleep(3)  # Pause for 3 seconds
    asyncio.run(run_worker())
