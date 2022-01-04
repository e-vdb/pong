"""Define a class for players"""


class Player:
    def __init__(self):
        self.can_play = False
        self.name = 'unknown'
        self.score = 0

    def reset(self):
        self.score = 0
        self.can_play = False
