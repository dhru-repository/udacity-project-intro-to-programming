import random

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.winCount = 0
        self.my_move = ""
        self.their_move = "rock"

    def learn(self, my_move, their_move):
        self.my_move = their_move

    def countScorePlayer(self, check):
        if check:
            self.winCount += 1
            print("Player 1 is the winner ")
        elif check:
            self.winCount += 1
            print("Player 2 is the winner.")

    def countScoreComputer(self, check):
        if check:
            self.winCount += 1
            print("Player 2 is the winner.")


# human plater
class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return validatePlayerChoice(input("rock, paper, scissors,"
                                          " lizard, spock? > "))


# computer only plays rock
class RockMoveComputer(Player):
    def move(self):
        return "rock"


# computer randomly pick a move per round.
class RandomMovesComputer(Player):
    def move(self):
        return random.choice(moves)


# computer loops through the available moves in the order that are in.
class LoopMovesComputer(Player):
    def __init__(self):
        super().__init__()
        self.choice = 4

    def move(self):
        options = moves
        if self.choice == 4:
            self.choice = 0
            return options[self.choice]
        elif self.choice == 0:
            self.choice = 1
            return options[self.choice]
        elif self.choice == 1:
            self.choice = 2
            return options[self.choice]
        elif self.choice == 2:
            self.choice = 3
            return options[self.choice]
        elif self.choice == 3:
            self.choice = 4
            return options[self.choice]


# computer copies player's previous round move
class ComputerImitatePlayer(Player):
    def __init__(self):
        super().__init__()

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.their_move = their_move
        return self.my_move

    def move(self):
        return self.learn(self.my_move, self.their_move)


# validate user's input for number
def validateRound(check):
    validate = True
    while validate:
        if not check.isnumeric():
            return validateRound(input("Please enter a number\n"))
        else:
            validate = False
            return int(check)


# game winning conditions
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'rock' and two == 'lizard') or
            (one == 'scissors' and two == 'paper') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'paper' and two == 'rock') or
            (one == 'paper' and two == 'spock') or
            (one == 'lizard' and two == 'spock') or
            (one == 'lizard' and two == 'paper') or
            (one == 'spock' and two == 'scissors') or
            (one == 'spock' and two == 'rock'))


# validate users input for correct response
def validatePlayerChoice(check):
    validate = True
    while validate:
        if check.lower() in moves:
            validate = False
            return check
        else:
            return validatePlayerChoice(input("Please enter rock, paper,"
                                              " scissors, lizard,"
                                              " or spock.\n"))


class Game:
    def __init__(self, p1, p2):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.tieGames = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 == move2:
            self.tieGames += 1
            print(f"Player 1: {move1}  Player 2: {move2}")
            print("Player 1 wins : ", self.p1.winCount,
                  "Player 2 Wins :", self.p2.winCount,
                  "\nTie games :", self.tieGames)
        else:
            print(f"Player 1: {move1}  Player 2: {move2}")
            self.p1.countScorePlayer(beats(move1, move2))
            self.p2.countScoreComputer(beats(move2, move1))
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)
            print("\nPlayer 1 wins : ", self.p1.winCount,
                  "Player 2 Wins :", self.p2.winCount)

    # play number of games depending on users input.
    def play_game(self, rounds):
        print("Game start!")
        for round in range(int(rounds)):
            print(f"\nRound {round + 1}:")
            self.play_round()
            if self.p1.winCount > self.p2.winCount:
                if round == int(rounds) - 1:
                    print("\nPlayer 1 is the winner of the Game!")
                    print("Player 1 wins : ", self.p1.winCount,
                          "Player 2 Wins :", self.p2.winCount)
            elif self.p2.winCount > self.p1.winCount:
                if round == int(rounds) - 1:
                    print("\nPlayer 2 is the Winner of the Game!")
                    print("Player 1 wins : ", self.p1.winCount,
                          "Player 2 Wins :", self.p2.winCount)
            else:
                if round == int(rounds) - 1:
                    print("\nNo winners tie games : ", int(rounds))
                    print("Player 1 wins : ", self.p1.winCount,
                          "Player 2 Wins :", self.p2.winCount)
            if round == int(rounds) - 1:
                print("Game over!, Number of rounds played : ", int(rounds))


if __name__ == '__main__':
    # choose random computer opponent for player to play against.
    randomOpponent = random.choice([RockMoveComputer(),
                                    RandomMovesComputer(),
                                    LoopMovesComputer(),
                                    ComputerImitatePlayer()])
    game = Game(HumanPlayer(), randomOpponent)
    print("Welcome to Rock, Paper,  Scissors, Lizard, Spock Game")
    game.play_game(validateRound(input(
        "How many rounds would you like to play?\n")))
