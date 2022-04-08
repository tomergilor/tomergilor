import requests

session = requests.session()

for i in range(10):
    r = session.get("http://127.0.0.1:1337/api/get_number" )
    print (r.json())