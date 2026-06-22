import os

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

PIXELA_USER = "lhgs"

PIXELA_GRAPHID = "d0loc0graph"
PIXELA_ENDPOINT = "https://pixe.la/v1/users/"
PIXELA_GRAPH_ENDPOINT = PIXELA_ENDPOINT + PIXELA_USER + "/graphs/"
PIXELA_PIXEL_ENDPOINT = PIXELA_GRAPH_ENDPOINT + PIXELA_GRAPHID

RESPONSE_SUCCESS = "Success."
RESPONSE_RETRY = "Please retry this request. Your request for some APIs will be rejected 25% of the time because you are not a Pixela supporter. If you are interested in being a Pixela supporter, please see: https://github.com/a-know/Pixela/wiki/How-to-support-Pixela-by-Patreon-%EF%BC%8F-Use-Limited-Features"
