# Project No.2#
# Authors: Grace DeGroot and Garrett Stroud
import random
import string


# Class representing a BoggleBoard
class BoggleBoard:
    def __init__(self, seed = None):
        self.board = []
        if seed is not None: # Sets random seed if specified
            random.seed(seed)


    # Method that randomly selects a letter from the alphabet
    def create_dice(self):
        dice = random.choice(string.ascii_uppercase)
        return dice

    # Method to generate board
    def fill_board(self):
        for row in range(4):
            row_vals = []
            for val in range(4):
                row_vals.append(self.create_dice())
            self.board.append(row_vals)
        return self.board

    # Method to print board
    def print_board(self):

        border = '+---+---+---+---+'

        for row in range(4):
            print(border)
            for col in range(4):
                print(f'| {self.board[row][col]} ', end="")
            print("|")
            print(border)

    # Method that prints board and highlights word
    def print_highlighted(self, path):
        print()
        border = '+---+---+---+---+'
        for row in range(4):
            print(border)

            for col in range(4):
                if (row,col)  in path:
                    print(f'|<{self.board[row][col]}>', end="")
                else:
                    print(f'| {self.board[row][col]} ', end="")

            print("|")
            print(border)


    # method to check users word guess
    def check_board(self, word):
        # find initial position and run recursion method from there
        word = word.upper()
        for row in range(4):
            for col in range(4):
                if self.board[row][col].upper() == word[0]:
                    path = []
                    if self.boggle_validation(word, 0, row, col,path):
                        return path
        
        return False

    # Recursive method that checks possible paths for the word
    def boggle_validation(self, word, index, row, col, path):
        # Base case
        if index == len(word):
            return True

        # Boundary restrictions
        if row < 0 or row > 3 or col < 0 or col > 3:
            return False

        if (row, col) in path:
            return False


        # Letter validation
        if self.board[row][col] != word[index]:
            return False
        
        path.append((row, col))


        # Directions representing adjacent tiles
        directions = [
        [0, -1],  # left
        [0, 1], # right
        [-1, 0], # above
        [1, 0] # below
        ]

        # Loops through every direction
        for r, c in directions:
            new_row = row + r
            new_col = col + c

            # Recursion method
            if self.boggle_validation(word, index + 1, new_row, new_col, path):
                return True

        # Returns False when all fails and remove last element
        path.pop()
        return False
