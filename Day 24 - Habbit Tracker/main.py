import requests
from datetime import datetime

TOKEN = "your_pixela_token"
USERNAME = "yout_username"

ID = "your_graph_id"

# creating a pixela account
pixela_endpoint = "https://pixe.la/v1/users"

usr_parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=usr_parameters)
# print(response.text)

# genrating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": ID,
    "name": "Study",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime.now()

# creating a data of pixel
pixel_creation_endpoint = f"{graph_endpoint}/{ID}"

pixel_creation_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes have you studied today? ")
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_params, headers=headers)
# print(response.text)

# updating a data if need
pixel_update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

pixel_update_params = {
    "quantity": "40"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

# deleting a data if need
pixel_delete_endpoint = f"{pixel_creation_endpoint}/20220325"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)