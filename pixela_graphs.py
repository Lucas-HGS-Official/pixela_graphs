import requests

from defines import PIXELA_GRAPH_ENDPOINT, PIXELA_GRAPHID, PIXELA_TOKEN, RESPONSE_SUCCESS


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
        response = pixela_response.json()["message"]


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
        response = pixela_response.json()["message"]


def chose_graph_action():
    actions_list = ["", "Create a graph", "Modify a graph", "Quit program"]
    for acts in actions_list[1:]:
        print(f"{acts} [{actions_list.index(acts)}]")
    user_input = int(input("\t"))

    if user_input == 1:
        create_graph()

    elif user_input == 2:
        modify_graph()
    elif user_input == 3:
        return
    else:
        return
