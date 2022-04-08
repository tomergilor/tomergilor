import requests

URL = "https://reqres.in/api/users/2"

# send Get request
response = requests.delete(URL)

# Fetch response code

print(response.status_code)
assert  response.status_code == 204


