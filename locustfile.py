import json

from locust import HttpUser, constant, task

IMAGE_URI = "https://fsdl-public-assets.s3-us-west-2.amazonaws.com/paragraphs/a01-077.png"


class TextRecognizerUser(HttpUser):
    wait_time = constant(1)
    headers = {"Content-type": "application/json"}
    payload = json.dumps({"image_url": IMAGE_URI})

    @task
    def predict(self):
        self.client.post("/", data=self.payload, headers=self.headers)
