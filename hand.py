from card import Card

class Hand:
    def __init__(self):
        self.hand = []
        
    def add_card(self, card: Card):
        self.hand.append(card)
        
    def get_score(self):
        score = sum(card.value() for card in self.hand)
        ace_count = sum(1 for card in self.hand if card.rank.value == 1)

        # 21 を超えている場合
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
            
        return score