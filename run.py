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
    Allows the player to make a guess on the board
    by entering row and column numbers.
    Updates the board based on the player's guess.
    """

    while True:
        try:
            x = int(input("Enter a number for row (1-5)\n")) - 1
            y = int(input("Enter a number for column (1-5)\n")) - 1
            # Check if the entered coordinates are valid
            if not valid_coordinates(x, y, board.size):
                print("Input is out of range. Enter a number between 1 and 5.")
            elif (x, y) in board.guesses:
                print("You have made a move in this position. Try again.")
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
    Simulates the gameplay between a computer and a player
    using two game boards.
    Tracks scores and prints the results until the game ends.
    """
    # Set to store computer's guessed coordinates
    computer_guesses = set()

    # Loop to continue the game until someone wins or it's a tie
    while True:
        print("Your board")
        player_board.print()
        print("Computer's board")
        computer_board.print()
        make_guess(computer_board)  # Player makes a guess on computer's board

        # Check if all ship coordinates are guessed
        # by the player on the computer's board
        if all(coord in computer_board.guesses for coord in computer_board.ships):
            print(f"Your score: {scores['player']}, Computer's score: {scores['computer']}")
            print(f"GAME OVER. {player_board.name} is the WINNER")
            print(f"Thank you for playing, {player_board.name}.")
            break

        # Ensures that the computer generates random coordinates
        # and avoids repeating guesses
        while True:
            x, y = random_point(computer_board.size), random_point(computer_board.size)
            if (x, y) not in computer_guesses:
                computer_guesses.add((x, y))
                break

        # Computer makes a guess on player's board
        result = player_board.add_guesses(x, y)
        if result == "Hit":
            print(f"Computer Hit at ({x+1}, {y+1})!")
            scores["computer"] += 1
            print(f"Your score: {scores['player']}, Computer's score: {scores['computer']}")
            print("=" * 70)
        else:
            print(f"Computer Missed at ({x+1}, {y+1})!")
            print(f"Your score: {scores['player']}, Computer's score: {scores['computer']}")
            print("=" * 70)

        # Check if all ship coordinates are guessed
        # by the computer on the player's board
        if all(coord in player_board.guesses for coord in player_board.ships):
            print(f"Your score: {scores['player']}, Computer's score: {scores['computer']}")
            print("GAME OVER. Computer is the WINNER")
            break

        # Check for a tie if both player and computer have a score of 3
        if scores['player'] == 3 and scores['computer'] == 3:
            print(f"Your score: {scores['player']}, Computer's score: {scores['computer']}")
            print("GAME OVER. It's a tie!")
            break


def play_again():
    """
    Ask user if they want to play again.
    """
    while True:
        play = input("Do you want to play again? (y/n): \n").lower()
        if play == "y":
            return True
        elif play == "n":
            print("Thank you for playing Battleships! Goodbye!")
            play = False  # Set the flag to False indicating not to play again
            break  # Break out of the loop
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def new_game():
    """
    Initialize and start a new game of Battleships.
    Initializes the game settings, boards, and starts the gameplay loop.
    """
    size = 5
    num_ships = 3
    scores["computer"] = 0
    scores["player"] = 0
    print("=" * 70)
    print("Welcome to Battleships Game!")

    print("Sink all of the ships before the oponent sinks them.")
    print("Missed ships are marked with 'M', hit ships are marked with'X")
    print("=" * 70)
    print(f"Board Size: {size}. Number of ships: {num_ships}")

    while True:
        print("=" * 70)
        player_name = input("Please enter your name: \n")
        if player_name:
            break
        else:
            print("Please enter a valid name!")

    # Create game boards for the computer and player
    computer_board = Board(size, num_ships, "Computer", "computer")
    player_board = Board(size, num_ships, player_name, "player")
    # Populate boards with ships
    populate_board(player_board)
    populate_board(computer_board)

    print("=" * 70)
    print(f"Greetings, {player_name}! Let's start the Battleship Game!")
    input("Press ENTER to start the game...\n")
    print("=" * 70)

    # Start the game by calling the play_game function
    # with the initialized boards
    play_game(computer_board, player_board)
    play_again()  # Ask if the players want to play again


# Start the game when the script is run
new_game()
