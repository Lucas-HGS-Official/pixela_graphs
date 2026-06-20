import requests

from defines import PIXELA_ENDPOINT, PIXELA_TOKEN, RESPONSE_SUCCESS


def create_user():
    response = ""
    while response != RESPONSE_SUCCESS:
        pixela_params = {
            "token": PIXELA_TOKEN,
            "username": "lhgs",
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        pixela_response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
        print(pixela_response.text)
        response = pixela_response.text
