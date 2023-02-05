import json
import os

from locust import HttpUser, constant, task

IMAGE_URI = "https://fsdl-public-assets.s3-us-west-2.amazonaws.com/paragraphs/a01-077.png"

try:
    API_KEY = os.environ["API_KEY"]
except KeyError:
    raise KeyError("Please set the API_KEY environment variable.")
try:
    MODEL_KEY = os.environ["MODEL_KEY"]
except KeyError:
    raise KeyError("Please set the MODEL_KEY environment variable.")


class TextRecognizerUser(HttpUser):
    wait_time = constant(1)
    headers = {"Content-type": "application/json"}
    payload = json.dumps({"apiKey": API_KEY, "modelKey": MODEL_KEY, "modelInputs": {"image": IMAGE_URI}})

    @task
    def predict(self):
        self.client.post("/", data=self.payload, headers=self.headers)
