from games.card import Card, Suit, Rank
import random


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Suit for rank in Rank]
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw_card(self):
        if not self.cards:
            raise ValueError("No more cards in the deck.")
        
        return self.cards.pop() 
    
    
    