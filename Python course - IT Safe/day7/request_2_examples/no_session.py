import requests


r = requests.get("http://127.0.0.1:1337/api/get_number")

for i in range(10):
    session = r.headers["Set-Cookie"].split(";")[0]
    session = session.split("=")
    cookie = {session[0]:session[1]}
    r = requests.get("http://127.0.0.1:1337/api/get_number", cookies=cookie)
    print (r.json())
