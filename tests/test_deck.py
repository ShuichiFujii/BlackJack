import pytest
from deck import Deck
from card import Card, Rank, Suit

@pytest.fixture
def deck():
    return Deck()

""" 
テストケース1: 正常系
- デッキの初期化
"""
def test_deck_init_success(deck):
    assert len(deck.cards) == 52
    assert all(isinstance(card, Card) for card in deck.cards)
    assert all(card.rank in Rank for card in deck.cards)
    assert all(card.suit in Suit for card in deck.cards)
    
""" 
テストケース2: 正常系
- カードを引く処理
"""
def test_draw_card_success(deck):
    initial_count = len(deck.cards)
    card = deck.draw_card()
    
    assert isinstance(card, Card)
    assert len(deck.cards) == initial_count - 1
    
""" 
テストケース3: 正常系
- シャッフルが成功する
"""
def test_deck_shuffle_success(deck):
    deck1 = Deck()
    deck2 = Deck()
    
    assert deck1.cards != deck2.cards
    
""" 
テストケース4: 異常系
- デッキが空の状態からカードを引く
"""
def test_draw_card_empty_deck(deck):
    # デッキから全てのカードを引く
    for _ in range(52):
        deck.draw_card()
        
    with pytest.raises(ValueError, match="No more cards in the deck."):
        deck.draw_card()