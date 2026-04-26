import pytest
from player import Player, PlayerStatus
from hand import Hand

"""
テストケース1: プレイヤーの初期化
"""
def test_player_init_success():
    player_id = 1
    status = PlayerStatus.PLAYER
    player = Player(status, player_id)
    
    assert player.player_id == player_id
    assert player.status == status
    assert isinstance(player.hand, Hand)
    assert len(player.hand.hand) == 0


"""
テストケース2: 不正な入力に対するバリデーション（異常系）
"""
@pytest.mark.parametrize("status, player_id, expected_msg", [
    ("NOT_ENUM_PLAYER_STATUS", 1, "status must be an instance of PlayerStatus Enum"),
    (PlayerStatus.PLAYER, "1", "player_id must be an integer"),
    (PlayerStatus.DEALER, None, "player_id must be an integer"),
])

def test_player_init_value_error(status, player_id, expected_msg):
    with pytest.raises(ValueError, match=expected_msg):
        Player(status, player_id)

"""
テストケース3: ディーラーとしての初期化
"""
def test_dealer_init():
    dealer = Player(PlayerStatus.DEALER, player_id=0)
    assert dealer.status == PlayerStatus.DEALER
    assert dealer.player_id == 0