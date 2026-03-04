# You should have a class called BoggleBoard, which includes the two-dimensional lists of letters,
# methods for filling and printing it, and a method that returns whether or not a given word is valid
# for the board. This last method should make use of another recursive method for verifying
# words.
import random
import string


class BoggleBoard:
    def __init__(self):
        self.board = []

    def create_dice(self):
        dice = random.choice(string.ascii_uppercase)
        return dice

    def fill_list(self):
        for row in range(4):
            row_vals = []
            for val in range(4):
                row_vals.append(self.create_dice())
            self.board.append(row_vals)
        return self.board


    def print_list(self):
        for row in self.board:
            print(row)

    def check_word(self, word):
        # find initial position and run recursion method from there
        path = [
            [False,False,False,False],
                [False,False,False,False],
                [False,False,False,False],
                [False,False,False,False]
        ]
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == word[0]:
                    if self.boggle_validation(word, 0, row, col,path):
                        return True
                    if path:
                        return path
        return False




    def boggle_validation(self,word,index,row,col,path):
        # Base case
        if index == len(word):
            return True

        # Boundary restrictions
        if row < 0 or row > 3 or col < 0 or col > 3:
            return False


        # Letter validation
        if self.board[row][col] != word[index]:
            return False

        # Return false if square has been visited already
        if path[row][col]:
            return False

        path[row][col] = True



        # Logic to check values around a box
        directions = [
            [0, -1],  # left
        [0, 1], # right
        [-1, 0], # above
        [1, 0] # below
        ]

        # Loops through every direction
        for r,c in directions:
            new_row = row + r
            new_col = col + c

            # Recursion method
            if self.boggle_validation(word,index+1,new_row,new_col,path):
                return True

        # Returns False when all fails
        path[row][col] = False
        return False








