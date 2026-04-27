from enum import Enum, auto
from games.hand import Hand

class PlayerStatus(Enum):
    PLAYER = auto()
    DEALER = auto()
    
class Player:
    def __init__(self, status: PlayerStatus, player_id: int):
        if not isinstance(status, PlayerStatus):
            raise ValueError("status must be an instance of PlayerStatus Enum")
        
        if not isinstance(player_id, int):
            raise ValueError("player_id must be an integer")
        
        self.player_id = player_id
        self.status = status
        self.hand = Hand()
    
    