import random


class rockScissorsPaper(object):
    def __init__(self):
        self.computer = 0
        self.user = 0

    def __str__(self):
        if self.user == 5:
            return "user win"
        else:
            return "computer win"

    def game(self, user_option):

        option = random.choice(['s','r','p'])
        if option == 's' and user_option == 'r':
            self.user += 1
        elif option == 's' and user_option == 'p':
            self.computer += 1

        elif option == 'r' and user_option == 'p':
            self.user += 1
        elif option == 'r' and user_option == 's':
            self.computer += 1

        elif option == 'p' and user_option == 's':
            self.user += 1
        elif option == 'p' and user_option == 'r':
            self.computer += 1

    def is_end(self):
        if self.user == 5 or self.computer == 5:
            return True
        else:
            return False


rsp = rockScissorsPaper()
while not rsp.is_end():
    rsp.game(input("[+] [r]ock [s]cissors [p]aper ? "))
else:
    print(rsp)
