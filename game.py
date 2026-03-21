from player import Player, PlayerStatus
from deck import Deck

class Game:
    def __init__(self, player_count: int):
        self.player_count = player_count
        self.deck = Deck()
        self.current_turn = 0
        self.players = [Player(PlayerStatus.PLAYER, player_id=i+1) for i in range(player_count)]
        self.dealer = Player(PlayerStatus.DEALER, player_id=0)
        self.__initial_cards()
        
    def __initial_cards(self):
        for _ in range(2):
            for player in self.players:
                card = self.deck.draw_card()
                player.hand.add_card(card)
                
            self.dealer.hand.add_card(self.deck.draw_card())
            
    def play(self):
        print(f"Dealer's first card: {self.dealer.hand.hand[0]}")
        
        for player in self.players:
            self.player_turn(player)
        
        self.dealer_turn()
        self.determine_winner()

    def player_turn(self, player):
        print(f"\n--- Player {player.player_id}'s Turn ---")
        while True:
            print(f"\nPlayer {player.player_id}'s hand: {self._format_hand(player)}")
            choice = input("Do you want to hit or stand? (h/s) ")
            
            if choice == "h":
                self._hit(player)
                if player.hand.get_score() > 21:
                    print(f"Bust! Player {player.player_id} loses with {player.hand.get_score()}.")
                    break
            elif choice == "s":
                print(f"Player {player.player_id} stands")
                break
            else:
                print("Invalid choice. Please enter 'h' or 's'.")

    def dealer_turn(self):
        print(f"\nDealer's second card: {self.dealer.hand.hand[1]}")
        while self.dealer.hand.get_score() < 17:
            self._hit(self.dealer)
            print(f"Dealer hits and draws {self.dealer.hand.hand[-1]}")
        print(f"Dealer stands with hand: {self._format_hand(self.dealer)}")

    def _hit(self, player):
        card = self.deck.draw_card()
        player.hand.add_card(card)
        return card

    def _format_hand(self, player):
        return ", ".join(str(card) for card in player.hand.hand)
        
    def determine_winner(self):
        dealer_score = self.dealer.hand.get_score()
        print(f"\n--- Final Results ---")
        print(f"Dealer's score: {dealer_score}")
        
        for player in self.players:
            player_score = player.hand.get_score()
            print(f"\nPlayer {player.player_id}'s score: {player_score}")
            
            # 1. プレイヤーがバーストしている場合（無条件で負け）
            if player_score > 21:
                print(f"Result: Player {player.player_id} BUSTED and loses.")
                
            # 2. ディーラーがバーストしている場合（生き残っているプレイヤーの勝ち）
            elif dealer_score > 21:
                print(f"Result: Dealer BUSTED! Player {player.player_id} wins!")
                
            # 3. どちらもバーストしていない場合はスコア勝負
            elif player_score > dealer_score:
                print(f"Result: Player {player.player_id} wins!")
                
            elif player_score < dealer_score:
                print(f"Result: Player {player.player_id} loses.")
                
            else:
                print(f"Result: Player {player.player_id} pushes (draw).")