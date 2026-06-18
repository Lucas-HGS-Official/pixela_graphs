import os

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

PIXELA_USER = "lhgs"

PIXELA_GRAPHID = "d0loc0graph"
PIXELA_ENDPOINT = "https://pixe.la/v1/users/"
PIXELA_GRAPH_ENDPOINT = PIXELA_ENDPOINT + PIXELA_USER + "/graphs/"
PIXELA_PIXEL_ENDPOINT = PIXELA_GRAPH_ENDPOINT + PIXELA_GRAPHID

RESPONSE_SUCCESS = '{"message":"Success.","isSuccess":true}'
