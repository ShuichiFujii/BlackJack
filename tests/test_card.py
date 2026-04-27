import pytest
from games.deck import Deck
from games.card import Card, Rank, Suit


""" 
テストケース1: 正常系
- カードの初期化
"""
def test_card_initialization():
    card = Card(Rank.ONE, Suit.DIAMOND)
    
    assert card.rank == Rank.ONE
    assert card.suit == Suit.DIAMOND

""" 
テストケース2: 正常系
- カードのスコア評価
- ACEは11点、10以上のカードは10点、それ以外はランクの値
"""
def test_evaluate_card_value():
    card1 = Card(Rank.ONE, Suit.HEART)
    card2 = Card(Rank.TEN, Suit.CLUB)
    card3 = Card(Rank.JACK, Suit.SPADE)
    card4 = Card(Rank.FIVE, Suit.SPADE)
    
    assert card1.value() == 11
    assert card2.value() == 10
    assert card3.value() == 10
    assert card4.value() == 5
            
""" 
テストケース3: 正常系
- カードの文字列表現
"""

def test_card_string_representation():
    card = Card(Rank.QUEEN, Suit.CLUB)
    assert str(card) == "12 of CLUB"
    
""" 
テストケース4: 異常系
- カードの初期化に無効なランクやスートを渡すと例外が発生する
"""
def test_card_invalid_initialization():
    with pytest.raises(ValueError, match="Rank must be an instance of Rank and Suit must be an instance of Suit."):
        Card("InvalidRank", Suit.HEART)
        Card(Rank.ONE, "InvalidSuit")