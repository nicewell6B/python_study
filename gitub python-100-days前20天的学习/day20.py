#目前这一章还不太看得懂以后再看

from enum import Enum

class Suite(Enum):
    SPADE, HEART, DIAMOND, CLUB = range(4)

for suite in Suite:
    print(f'{suite}: {suite.value}')

class Card:
    def __init__(self, suite, face):
        self.suit = suite
        self.face = face

    def __repr__(self):
        suites= '♠♥♣♦'
        faces = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return f'{suites[self.suite.value]}{faces[self.face]}'


card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1)
print(card2)

import random


class Poket:

