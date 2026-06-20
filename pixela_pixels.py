from datetime import datetime

import requests

from defines import PIXELA_PIXEL_ENDPOINT, PIXELA_TOKEN, RESPONSE_SUCCESS


def create_pixel(quantity: str):
    response = ""
    while response != RESPONSE_SUCCESS:
        today = datetime.now()
        pixela_params = {
            "date": str(today.strftime("%Y%m%d")),
            "quantity": quantity,
        }
        headers = {
            "X-USER-TOKEN": PIXELA_TOKEN,
        }
        pixela_response = requests.post(
            url=PIXELA_PIXEL_ENDPOINT, json=pixela_params, headers=headers
        )
        print(pixela_response.text)
        response = pixela_response.text


def add_to_pixel(quantity: str):
    response = ""
    while response != RESPONSE_SUCCESS:
        today = datetime.now()
        formatted_today = str(today.strftime("%Y%m%d"))
        pixela_params = {"quantity": quantity}
        headers = {"X-USER-TOKEN": PIXELA_TOKEN}
        pixela_response = requests.put(
            url=PIXELA_PIXEL_ENDPOINT + "/" + formatted_today + "/add",
            json=pixela_params,
            headers=headers,
        )
        print(pixela_response.text)
        response = pixela_response.text
