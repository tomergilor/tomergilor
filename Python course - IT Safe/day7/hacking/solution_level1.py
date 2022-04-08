import pytesseract
import requests


def get_captcha():
    r = session.get(url + "stage2.php", stream=True)

    for line in r.iter_lines():
        line = str(line)
        if "captcha_image" in line:
            image_path =  line[line.rfind("img"):line.find("png") + 3]
            break

    r = session.get(url + image_path)
    with open("a.png", 'wb') as f:
        f.write(r.content)

    return pytesseract.image_to_string("a.png")


def submit_captcha():
    headers = {"content-type":"application/x-www-form-urlencoded"}
    r = session.post(url + "api.php", headers=headers, data="captcha={0}&chal=stage2".format(captcha))
    if "You did it" in r.text:
        print (r.text)
        return True
    else:
        return False


url = "https://challenges.itsafe.co.il/PYTHON/"
session = requests.session()
counter = 0

while True:
    counter +=1
    captcha = get_captcha()
    if submit_captcha():
        break

print ("Tries: ", counter)



