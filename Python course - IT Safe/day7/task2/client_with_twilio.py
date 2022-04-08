from twilio.rest import Client
import requests
import time


url = "http://127.0.0.1:1337/index.html"
old_site = ""
r = requests.get(url)
old_site = r.text


while True:
    time.sleep(1)
    r = requests.get(url)
    if old_site != r.text:
        print("new website! send sms!")

        account_sid = 'AC3dd93b70cd50ae261b91e54dd9afa7e6'
        auth_token = 'a6351b8895bf3452d7ff9c8e30093554'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="I sending this from python!",
            from_='+12052739757',
            to='+972548632232'
        )

        print(message.sid)
        break
