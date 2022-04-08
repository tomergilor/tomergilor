import random


class CrazyPlane:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update_position(self):
        self.x += random.randint(-1,1)
        self.y += random.randint(-1,1)

    def get_position(self):
        return self.x, self.y

