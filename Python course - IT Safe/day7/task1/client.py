import requests
import json

session = requests.session()
data = {"guess":0}
header = {"content-type": "application/json"}

r = session.get("http://127.0.0.1:1337/api/start_game")
if r.json()["success"]:
    while True:
        data["guess"] = input("Guess the number > ")
        r = session.post("http://127.0.0.1:1337/api/guess_the_number", data=json.dumps(data), headers=header)

        json_data = r.json()
        print(json_data)
        if json_data["status"] == "you win":
            break
else:
    print("Can't Play the Game")