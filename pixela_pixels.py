from datetime import datetime

import requests

from defines import PIXELA_PIXEL_ENDPOINT, PIXELA_TOKEN, RESPONSE_SUCCESS


def create_pixel(quantity: str, date: str):
    response = ""
    while response != RESPONSE_SUCCESS:
        pixela_params = {
            "date": date,
            "quantity": quantity,
        }
        headers = {
            "X-USER-TOKEN": PIXELA_TOKEN,
        }
        pixela_response = requests.post(
            url=PIXELA_PIXEL_ENDPOINT, json=pixela_params, headers=headers
        )
        print(pixela_response.text)
        response = pixela_response.json()["message"]


def add_to_pixel(quantity: str, date: str):
    response = ""
    while response != RESPONSE_SUCCESS:
        pixela_params = {"quantity": quantity}
        headers = {"X-USER-TOKEN": PIXELA_TOKEN}
        pixela_response = requests.put(
            url=PIXELA_PIXEL_ENDPOINT + "/" + date + "/add",
            json=pixela_params,
            headers=headers,
        )
        print(pixela_response.text)
        response = pixela_response.json()["message"]


def chose_date():
    user_input = input("Is it for today? (y/n)\n\t")
    if user_input == "y":
        return str(datetime.now().strftime("%Y%m%d"))
    else:
        date = ""
        date += input("For what year? (Four digits)\n\t")
        date += input("For what month? (Two digits)\n\t")
        date += input("For what day? (Two digits)\n\t")
        if date == str(datetime.now().strftime("%Y%m%d")):
            print("work")
        return date


def chose_pixel_action():
    actions_list = ["Create a pixel", "Add to a pixel", "Quit program"]
    for acts in actions_list:
        print(f"{acts} [{actions_list.index(acts)}]")
    user_input = int(input("\t"))

    if user_input == 0:
        quantity = input("How many for the pixel:\n\t")
        create_pixel(quantity, chose_date())

    elif user_input == 1:
        quantity = input("How many to add to the pixel\n\t")
        add_to_pixel(quantity, chose_date())
    elif user_input == 3:
        return
