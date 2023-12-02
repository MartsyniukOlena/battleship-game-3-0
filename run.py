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