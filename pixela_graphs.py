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
