from games.game import Game


if __name__ == "__main__":
    player_count = int(input("Enter the number of players: "))
    game = Game(player_count=player_count)
    game.play()