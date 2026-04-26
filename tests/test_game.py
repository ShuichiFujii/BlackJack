from game import Game


class FakeCard:
    def __str__(self):
        return "Ace of Spades"


class FakeDeck:
    def draw_card(self):
        return FakeCard()


class FakeHand:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_score(self):
        return 20


class FakePlayer:
    def __init__(self):
        self.player_id = 1
        self.hand = FakeHand()


class FakeDisplay:
    def __init__(self):
        self.messages = []

    def show_message(self, message):
        self.messages.append(message)


class FakeScoreHand:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score


class FakeScorePlayer:
    def __init__(self, player_id, score):
        self.player_id = player_id
        self.hand = FakeScoreHand(score)


def test_hit_adds_card_to_player_hand():
    game = Game.__new__(Game)
    game.deck = FakeDeck()

    player = FakePlayer()

    card = game._hit(player)

    assert str(card) == "Ace of Spades"
    assert len(player.hand.hand) == 1


def test_format_hand_success():
    game = Game.__new__(Game)

    card1 = FakeCard()
    card2 = FakeCard()

    player = FakePlayer()
    player.hand.hand = [card1, card2]

    result = game._format_hand(player)

    assert result == "Ace of Spades\nAce of Spades"


def test_determine_winner_player_wins():
    game = Game.__new__(Game)

    game.display = FakeDisplay()
    game.players = [FakeScorePlayer(player_id=1, score=20)]
    game.dealer = FakeScorePlayer(player_id=0, score=18)

    game.determine_winner()

    assert "Result: Player 1 wins!" in game.display.messages


def test_determine_winner_player_busts():
    game = Game.__new__(Game)

    game.display = FakeDisplay()
    game.players = [FakeScorePlayer(player_id=1, score=22)]
    game.dealer = FakeScorePlayer(player_id=0, score=18)

    game.determine_winner()

    assert "Result: Player 1 BUSTED and loses." in game.display.messages