from flask import Flask, request, jsonify
import asyncio
from temporalio import workflow
from temporal_workflows.workflow import MyWorkflow
from temporalio.client import Client
import os

app = Flask(__name__)
app.config["DEBUG"] = True

temporal_service_address = os.getenv('TEMPORAL_SERVICE_ADDRESS', 'host.docker.internal:7233')
print("Temporal service address: " + temporal_service_address)


async def start_workflow(input_data):
    client = await Client.connect(temporal_service_address, namespace="default")
    return await client.execute_workflow(MyWorkflow.run, input_data, id="workflow-id", task_queue="hello-task-queue")


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200


@app.route('/start-workflow', methods=['POST'])
def trigger_workflow():
    input_data = request.json
    result = asyncio.run(start_workflow(input_data))
    return jsonify({"workflow_result": str(result)})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
