import requests
import json
import jsonpath


URL = "https://reqres.in/api/users/2"

# Read Input Json file:

file = open('C:\\API_REQ\\new_user.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with json input body

response = requests.put(URL, request_json)

# validate response

assert response.status_code == 200
print(response.status_code)


# Parse response content:
response_json = json.loads(response.text)
update_li = jsonpath.jsonpath(response_json, 'updatedAt')
