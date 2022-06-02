from enum import Enum


"""
트럼프 카드 하나를 뜻함
"""
class Card:
    def __init__(self, shape, number):
        self.shape = shape
        self.number = number

    def randomize(self):



class Shape(Enum):
    SPADE = 0
    HEART = 1
    CLOVER = 2
    DIAMOND = 3
    # 홀수는 검은색
    # 짝수는 빨간색


class SpecialNumber(Enum):
    ACE = 1
    KING = 2
    QUEEN = 3
    JACK = 4
    TWO = 5
    THREE = 6
    FOUR = 7
    FIVE = 8
    SIX = 9
    SEVEN = 10
    EIGHT = 11
    NINE = 12
    TEN = 13