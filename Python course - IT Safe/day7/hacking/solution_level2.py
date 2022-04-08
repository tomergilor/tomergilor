import pytesseract
import requests
import string
from PIL import Image


def get_captcha():
    r = session.get(url + "stage2.php?level=2", stream=True)

    for line in r.iter_lines():
        line = str(line)
        if "captcha_image" in line:
            image_path =  line[line.rfind("img"):line.find("png") + 3]
            break

    r = session.get(url + image_path)
    with open("a.png", 'wb') as f:
        f.write(r.content)

    with Image.open('a.png') as captcha_file:
        width, height = captcha_file.size

        for i in range(height):
            for k in range(width):
                if captcha_file.getpixel((k, i)) == (255, 255, 255):
                    captcha_file.putpixel((k, i), (0, 0, 0))
                else:
                    captcha_file.putpixel((k, i), (255, 255, 255))

    captcha_file.save("captcha2.png")
    text = pytesseract.image_to_string("captcha2.png")

    output = []
    for character in text:
        if character in string.ascii_letters:
            output.append(character)

    return "".join(output)


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
    print (captcha)
    if submit_captcha():
        break

print ("Tries: ", counter)