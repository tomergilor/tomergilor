import random


class guessTheNumber(object):
    count = 0
    def __init__(self):
        guessTheNumber.count+=1
        self.number = random.randint(0, 1000)
        self.tries = 0

    def __call__(self, *args, **kwargs):
        number = kwargs["number"]
        if number > self.number:
            print ("you number is bigger")
            self.tries +=1
            return False

        elif number < self.number:
            print("you number is smaller")
            self.tries += 1
            return False

        else:
            return True

while True:
    number = int(input("[+] Guess the number  -1 to exit> "))
    if number == -1:
        break

    game = guessTheNumber()
    while not game(number=number):
        number = int(input("[+] Guess the number > "))
    else:
        print ("You win in {0}".format(game.tries))

print ("Game End in {0}".format(game.count))

