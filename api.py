import requests
import os
import json
from dotenv import load_dotenv
import time

# TODO write unit tests

load_dotenv()
application_uuid = os.environ["CAMERALYZE_APPLICATION_UUID"]
api_key = os.environ["CAMERALYZE_API_KEY"]


# TODO handle request fail scenarios

def detect_humans(img):
    api_call = requests.post("https://platform.api.cameralyze.com/application/triggers/programatic/run",
                             json={"applicationUuid": application_uuid, "apiKey": api_key, "image": img})

    response = api_call.json()

    return response


def get_results(job_id):
    api_call = requests.post('https://platform.api.cameralyze.com/application/triggers/programatic/result/get',
                             json={"apiKey": api_key, "jobId": job_id})
    response = api_call.json()

    return response
def check(encoded_string):
    response = detect_humans(encoded_string)

    job_id = response['data']['job_id']

    status = 0

    while not status == 200:
        print("Checking for results...")
        time.sleep(0.1)
        response = get_results(job_id)
        status = response['status']
        print(status == 200 and "Results found!" or "No results yet")

    data = json.dumps(response['data'])
    return data