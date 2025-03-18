import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

class Game:
    def __init__(self, num_players=2):
        random.seed(0)
        self.die = Die()
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.current_player = 0

    def switch_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def play_turn(self, player):
        turn_total = 0
        print(f"{player.name}'s turn!")
        while True:
            roll = self.die.roll()
            print(f"{player.name} rolled a {roll}")
            if roll == 1:
                print(f"{player.name} loses all points for this turn!")
                break
            turn_total += roll
            print(f"Current turn total: {turn_total}, Total score: {player.score}")
            decision = input("Roll (r) or Hold (h)? ").strip().lower()
            if decision == 'h':
                player.add_score(turn_total)
                break
        print(f"{player.name}'s total score is now {player.score}\n")

    def check_winner(self):
        for player in self.players:
            if player.score >= 100:
                print(f"{player.name} wins with {player.score} points!")
                return True
        return False

    def run(self):
        print("Welcome to Pig Dice Game!")
        while True:
            self.play_turn(self.players[self.current_player])
            if self.check_winner():
                break
            self.switch_turn()
        print("Game Over!")

if __name__ == "__main__":
    num_players = int(input("Enter number of players: "))
    game = Game(num_players)
    game.run()

