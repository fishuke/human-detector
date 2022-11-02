import json
import base64
import pandas
import time

from api import detect_humans, get_results


def main():
    with open("photo.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf8")

    # TODO handle request fail scenarios
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
    pandas.read_json(path_or_buf=data, orient='split').to_excel("output.xlsx", index=False)
    print("Excel file created!")


if __name__ == '__main__':
    main()
