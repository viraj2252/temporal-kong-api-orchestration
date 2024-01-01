from temporalio import workflow, activity
from datetime import timedelta
import requests


@workflow.defn(sandboxed=False)
class MyWorkflow:
    @workflow.run
    async def run(self, input_data):
        result1 = await workflow.execute_activity(activity1, input_data,
                                                  start_to_close_timeout=timedelta(seconds=5))
        result2 = await workflow.execute_activity(activity2, result1,
                                                  start_to_close_timeout=timedelta(seconds=5))
        return result2


@activity.defn
async def activity1(input_data):
    try:
        response = requests.get("https://cat-fact.herokuapp.com/facts/")
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text  # Return the response content as a string
    except requests.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")
        return "processed_by_activity1"


@activity.defn
async def activity2(input_data):
    try:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return input_data + " ################ \r\n" + response.text  # Return the response content as a string
    except requests.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")
        return input_data + "_and_activity2"
