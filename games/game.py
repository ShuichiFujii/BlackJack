from games.player import Player, PlayerStatus
from games.deck import Deck

class GameDisplay:
    def show_status(self, name, hand_text, score):
        print(f"\n--- {name}'s Status ---\n")
        print(f"{name}'s hand:")
        print(hand_text)
        print(f"Current score: {score}\n")
        
    def show_message(self, message):
        print(message)
        
    def ask_hit_or_stand(self):
        return input("Do you want to hit or stand? (h/s): ").lower().strip()
    
    
class Game:
    def __init__(self, player_count: int):
        self.deck = Deck()
        self.display = GameDisplay()
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
        self.display.show_message(f"Dealer's first card: {self.dealer.hand.hand[0]}")
        
        for player in self.players:
            self.player_turn(player)
        
        self.dealer_turn()
        self.determine_winner()
        
    def player_turn(self, player):
        name = f"Player {player.player_id}"
        
        while True:
            self.display.show_status(
                name=name, 
                hand_text=self._format_hand(player),
                score=player.hand.get_score()
            )
            
            choice = self.display.ask_hit_or_stand()
            
            if choice == "h":
                self._hit(player)
                if player.hand.get_score() > 21:
                    self.display.show_message(
                        f"Bust! {name} loses with {player.hand.get_score()}."
                    )
                    break
                
            elif choice == "s":
                self.display.show_message(
                    f"Stand! {name} stands with {player.hand.get_score()}."
                )
                break
            
            else:
                self.display.show_message("Invalid choice. Please enter 'h' or 's'.")

    def dealer_turn(self):
        self.display.show_message(f"\nDealer's second card:\n{self.dealer.hand.hand[1]}")
        self.display.show_status(
            name="Dealer", 
            hand_text=self._format_hand(self.dealer),
            score=self.dealer.hand.get_score()
        )
        
        while self.dealer.hand.get_score() < 17:
            card = self._hit(self.dealer)
            self.display.show_message(f"Dealer hits and draws {card}")
        self.display.show_message(f"Dealer stands with hand:\n{self._format_hand(self.dealer)}")

    def _hit(self, player):
        card = self.deck.draw_card()
        player.hand.add_card(card)
        return card

    def _format_hand(self, player):
        return "\n".join(str(card) for card in player.hand.hand)
    
    def determine_winner(self):
        dealer_score = self.dealer.hand.get_score()
        self.display.show_message(f"\n--- Final Results ---")
        self.display.show_message(f"Dealer's score: {dealer_score}\n")
        
        for player in self.players:
            player_score = player.hand.get_score()
            self.display.show_message(f"Player {player.player_id}'s score: {player_score}")
            
            # 1. プレイヤーがバーストしている場合（無条件で負け）
            if player_score > 21:
                self.display.show_message(f"Result: Player {player.player_id} BUSTED and loses.")
                
            # 2. ディーラーがバーストしている場合（生き残っているプレイヤーの勝ち）
            elif dealer_score > 21:
                self.display.show_message(f"Result: Dealer BUSTED! Player {player.player_id} wins!")
                
            # 3. どちらもバーストしていない場合はスコア勝負
            elif player_score > dealer_score:
                self.display.show_message(f"Result: Player {player.player_id} wins!")
                
            elif player_score < dealer_score:
                self.display.show_message(f"Result: Player {player.player_id} loses.")
                
            else:
                self.display.show_message(f"Result: Player {player.player_id} pushes (draw).")
                
            print()