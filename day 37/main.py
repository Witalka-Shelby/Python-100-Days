import requests
from datetime import datetime

TOKEN = "asdsdfsdf"
USERNAME = "witalka"
ID = "graph1"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_url = "https://pixe.la/v1/users"

response = requests.post(url=pixela_url, json=params)

# print(response.text)

graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"

graph_conf = {
    "id": ID,
    "name": "python",
    "unit": "days",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response_graph = requests.post(url=graph_endpoint, json=graph_conf, headers=headers)

# print(response_graph.text)


pixel_url = f"{pixela_url}/{USERNAME}/graphs/{ID}"

today = datetime.now()
date_pixel = today.strftime("%Y%m%d")

add_pixel = {
    "date": date_pixel,
    "quantity": "1",
}


response_pixel = requests.post(pixel_url, headers=headers, json=add_pixel)

# print(response_pixel.text)

update_pixel_url = f"{pixela_url}/{USERNAME}/graphs/{ID}/{date_pixel}"

update_pixel_config = {
    "quantity": "14"
}

response_update = requests.put(url=update_pixel_url, headers=headers, json=update_pixel_config)

print(response_update.text)