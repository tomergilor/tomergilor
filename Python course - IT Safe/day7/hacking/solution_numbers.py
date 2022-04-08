import requests


def get_challenge():
    r = session.get(url, stream=True)
    for line in r.iter_lines():
        line = str(line)
        if '<h3 class="text-center">' in line:
            return line[line.rfind(" ")+1:line.find("</h3>")]


def solve_challenge(solution):
    r = session.post(solv_url, data="solution={0}&chal=stage1&".format(solution), headers=header, stream=True)
    for line in r.iter_lines():
        line = str(line)
        if 'solved' in line or "You" in line:
            print (line)


session = requests.session()
header = {"content-type":"application/x-www-form-urlencoded"}
solv_url = "https://challenges.itsafe.co.il/PYTHON/api.php"
url = "https://challenges.itsafe.co.il/PYTHON/stage1.php"

for i in range(10):
    try:
        challenge = get_challenge()
        solution = eval(challenge)
        solve_challenge(solution)
    except:
        pass