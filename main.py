import os
from datetime import datetime

import requests

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USER = "lhgs"
PIXELA_GRAPHID = "d0loc0graph"
PIXELA_ENDPOINT = "https://pixe.la/v1/users/"
PIXELA_GRAPH_ENDPOINT = PIXELA_ENDPOINT + PIXELA_USER + "/graphs/"
PIXELA_PIXEL_ENDPOINT = PIXELA_GRAPH_ENDPOINT + PIXELA_GRAPHID

RESPONSE_SUCCESS = '{"message":"Success.","isSuccess":true}'


def main():
    if __name__ == "__main__":
        current_use = input(
            "Options:\n\tcreate_user\n\tcreate_graph\n\tmodify_graph\n\tcreate_pixel_today\n\taddto_pixel_today\n\tquit\n\t\t"
        )
        # Generate Pixela user #
        if current_use == "create_user":
            create_user()
            # https://pixe.la/@lhgs
        #########################

        # Generate a graph
        elif current_use == "create_graph":
            create_graph()
            # https://pixe.la/v1/users/lhgs/graphs/d0loc0graph.html
        #########################

        # Generate a day pixel
        elif current_use == "create_pixel_today":
            quantity = input("how many for the pixel\n\t")
            create_pixel(quantity)
        #########################

        # Add to a day pixel
        elif current_use == "addto_pixel_today":
            quantity = input("how many to add to the pixel\n\t")
            add_to_pixel(quantity)
        #########################

        # Update Graph
        elif current_use == "modify_graph":
            modify_graph()
        #########################

        elif current_use == "quit":
            return

        print("https://pixe.la/v1/users/lhgs/graphs/d0loc0graph.html")


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


def create_graph():
    response = ""
    while response != RESPONSE_SUCCESS:
        pixela_params = {
            "id": "d0loc0graph",
            "name": "Daily Lines of Code",
            "unit": "LOC",
            "type": "int",
            "color": "momiji",
        }
        headers = {
            "X-USER-TOKEN": PIXELA_TOKEN,
        }
        pixela_response = requests.post(
            url=PIXELA_GRAPH_ENDPOINT, json=pixela_params, headers=headers
        )

        print(pixela_response.text)
        response = pixela_response.text


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


def modify_graph():
    response = ""
    while response != RESPONSE_SUCCESS:
        pixela_params = {"timezone": "America/Sao_Paulo"}
        headers = {"X-USER-TOKEN": PIXELA_TOKEN}
        pixela_response = requests.put(
            url=PIXELA_GRAPH_ENDPOINT + PIXELA_GRAPHID,
            json=pixela_params,
            headers=headers,
        )
        print(pixela_response.text)
        response = pixela_response.text


main()
