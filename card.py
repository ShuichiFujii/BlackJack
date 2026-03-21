from enum import Enum, auto

class Suit(Enum):
    HEART = auto()
    DIAMOND = auto()
    CLUB = auto()
    SPADE = auto()


class Rank(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        if not isinstance(rank, Rank) or not isinstance(suit, Suit):
            raise ValueError("Rank must be an instance of Rank and Suit must be an instance of Suit.")
        
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f"{self.rank.value} of {self.suit.name}"
    
    def value(self):
        if self.rank.value >= 10:
            return 10
        
        elif self.rank.value == 1:
            return 11
        
        return self.rank.value
    