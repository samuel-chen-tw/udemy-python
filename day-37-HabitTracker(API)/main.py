import requests
from datetime import datetime

USERNAME = "samuelchen"
TOKEN = "abcdefghijk"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

grpah_config = {
    "id": GRAPH_ID,
    "name": "running Graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=grpah_config, headers=headers)
# print(response.text)

record_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=8, day=1)
print(today.strftime("%Y%m%d"))

record_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

# response = requests.post(url=record_graph, json=record_params, headers=headers)
# print(response.text)


update_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230728"

update_params = {
    "quantity": "5.1"
}

# response = requests.put(url=update_graph, json=update_params, headers=headers)
# print(response.text)

delete_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230728"

response = requests.put(url=delete_graph, headers=headers)
print(response.text)
