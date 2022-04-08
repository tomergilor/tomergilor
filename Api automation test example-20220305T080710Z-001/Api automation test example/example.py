import requests
import json
import jsonpath


BASE_URL = "https://reqres.in"

# send Get request
response = requests.get(BASE_URL + "/api/users?page=2")

# validate status code
assert (response.status_code == 200)

print(response)
print(response.json())
print("_______________________________________")
print(json.dumps(response.json(), indent=4))
print("_______________________________________")

# Fetch response Header:

print(response.headers)
print(response.headers.get("Date"))
print(response.headers.get("Server"))

# Fetch Cookies:
print(response.cookies)

# Fetch Encoding:
print(response.encoding)

print(response.elapsed)

print ("---------------------------------------------")

# Parse response to Json format:
json_response = json.loads(response.text)
print(json_response)

# Fetch value using Json Path:
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])

# Fetch value using Json Path:

for i in range (0,3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print((first_name[0]))
