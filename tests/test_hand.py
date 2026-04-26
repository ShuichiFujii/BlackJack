import pytest
from hand import Hand
from card import Card, Rank, Suit

@pytest.fixture
def hand():
    return Hand()

""" 
テストケース: 加算処理

- エース無し
- 空の手札
- ブラックジャック
- エースを11として計算
- エースを1として計算
- 4枚のエース
"""
@pytest.mark.parametrize("ranks, expected_score", [
    ([Rank.TEN, Rank.FIVE], 15), 
    ([], 0),
    ([Rank.ONE, Rank.TEN], 21), 
    ([Rank.ONE, Rank.NINE], 20), 
    ([Rank.ONE, Rank.TEN, Rank.FIVE], 16), 
    ([Rank.ONE, Rank.ONE, Rank.ONE, Rank.ONE], 14), 
])

def test_hand_scores(hand, ranks, expected_score):
    for rank in ranks:
        hand.add_card(Card(rank, Suit.SPADE)) # スートは何でもOK
    
    assert hand.get_score() == expected_score
    
    
""" 
テストケース2: 不正なカードの追加

- カードオブジェクト以外を追加しようとする
"""
def test_add_card_invalid_type(hand):
    with pytest.raises(TypeError, match="card must be an instance of Card"):
        hand.add_card("not a card")