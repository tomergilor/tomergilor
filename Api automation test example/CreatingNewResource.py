import requests
import json


URL = "https://reqres.in/api/users"

# Read Input Json file:

file = open('C:\\API_REQ\\new_user.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with json input body

response = requests.post(URL, request_json)

# validate response

assert response.status_code == 201
print(response.status_code)
