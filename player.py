from enum import Enum, auto
from hand import Hand

class PlayerStatus(Enum):
    PLAYER = auto()
    DEALER = auto()
    
class Player:
    def __init__(self, status: PlayerStatus, player_id: int):
        self.player_id = player_id
        self.status = status
        self.hand = Hand()
    
    