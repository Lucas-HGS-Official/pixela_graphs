import requests

from defines import PIXELA_ENDPOINT, PIXELA_TOKEN, RESPONSE_SUCCESS


def create_user(user_name: str):
    response = ""
    while response != RESPONSE_SUCCESS:
        pixela_params = {
            "token": PIXELA_TOKEN,
            "username": user_name,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        pixela_response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
        print(pixela_response.text)
        response = pixela_response.json()["message"]


def chose_user_acttion():
    actions_list = ["", "Create a user", "quit"]
    for acts in actions_list[1:]:
        print(f"{acts} [{actions_list.index(acts)}]")
    user_input = int(input("\t"))

    if user_input == 1:
        create_user(input("What will be the user name?"))
    elif user_input == 2:
        return
    else:
        return
