# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Importing the randint function from the random module
from random import randint


# Scores for both computer and player
scores = {"computer": 0, "player": 0}


class Board:
    """
    Main Board class. Sets board size, the number of ships,
    the player's name and the board type (player board or computer)
    Has methods for adding ships and guesses and printing the board
    """
    def __init__(self, size, num_ships, name, type1):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type1
        self.guesses = []
        self.ships = []

    def print(self):
        """
        Print the board with ships and guesses.
        """
        print("  " + "  ".join(str(i) for i in range(1, self.size + 1)))
        for i, row in enumerate(self.board, start=1):
            print(i, "  ".join(row))

    def add_guesses(self, x, y):
        """
        Add player's guesses to the board.
        """
        self.guesses.append((x, y))
        self.board[x][y] = "M"

        if (x, y) in self.ships:
            self.board[x][y] = "X"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y):
        """
        Add ships to the board.
        """
        self.ships.append((x, y))
        if self.type == "player":
            self.board[x][y] = "S"


def random_point(size):
    """
    Generate random coordinate within board size.
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, size):
    """
    Check if coordinates are within the board.
    """
    return 0 <= x < size and 0 <= y < size


def populate_board(board):
    """
    Populate the board with ships.
    """
    for _ in range(board.num_ships):
        while True:
            x = random_point(board.size - 1)
            y = random_point(board.size - 1)
            if (x, y) not in board.ships:
                board.add_ship(x, y)
                break


def make_guess(board):
    """
    Allows the player to make a guess on the board by entering row and column numbers.
    Updates the board based on the player's guess.
    """

    while True:
        try:
            x = int(input("Enter a number for row (1-5)")) - 1
            y = int(input("Enter a number for column (1-5)")) - 1
            # Check if the entered coordinates are valid
            if not valid_coordinates(x, y, board.size):
                print("Input is out of range. Enter a number between 1 and 5.")
            elif (x, y) in board.guesses:
                print("You have already made a move in this position. Try again.")
            else:
                # Add the guess to the board and check the result
                result = board.add_guesses(x, y)
                if result == "Hit":
                    print("Boom! You hit! A ship has exploded!")
                    scores["player"] += 1
                else:
                    print("You Missed!")
                break
        except ValueError:
            print("Only enter numbers!")


def play_game(computer_board, player_board):
    """
    Simulates the gameplay between a computer and a player using two game boards.
    Tracks scores and prints the results until the game ends.
    """
    # Set to store computer's guessed coordinates
    computer_guesses = set()

play_game(computer_board, player_board)