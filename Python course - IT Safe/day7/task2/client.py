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
        break