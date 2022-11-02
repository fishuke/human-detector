import requests
import os

from dotenv import load_dotenv

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
