# You should have a class called BoggleBoard, which includes the two-dimensional lists of letters,
# methods for filling and printing it, and a method that returns whether or not a given word is valid
# for the board. This last method should make use of another recursive method for verifying
# words.
import random
import string


class BoggleBoard:
    def __init__(self,seed = None):
        self.board = []
        if seed is not None:
            random.seed(seed)

    def get_seed(self,seed):
        return random.seed(seed)

    def create_dice(self):
        dice = random.choice(string.ascii_uppercase)
        return dice

    def fill_board(self):
        for row in range(4):
            row_vals = []
            for val in range(4):
                row_vals.append(self.create_dice())
            self.board.append(row_vals)
        return self.board


    def print_board(self):

        border = '+---+ +---+ +---+ +---+'

        for row in range(4):
            print(border)
            for col in range(4):
                print(f'| {self.board[row][col]} |', end=" ")
            print()
            print(border)

    def print_highlighted(self, path):
        border = '+---+ +---+ +---+ +---+'

        for row in range(4):
            print(border)
            for col in range(4):

                # If the letter is in path then highlight
                if (row, col) in path:
                    print(f'[<{self.board[row][col]}>]', end=" ")
                else:
                    print(f'| {self.board[row][col]} |', end=" ")

            print()
            print(border)











    def check_board(self, word):
        # find initial position and run recursion method from there

        for row in range(4):
            for col in range(4):
                if self.board[row][col].upper() == word[0]:
                    path = []
                    if self.boggle_validation(word, 0, row, col,path):
                        return path

        return False





    def boggle_validation(self,word,index,row,col,path):
        # Base case
        if index == len(word):
            return True

        # Boundary restrictions
        if row < 0 or row > 3 or col < 0 or col > 3:
            return False

        if (row, col) in path:
            return False

        path.append((row, col))


        # Letter validation
        if self.board[row][col] != word[index]:
            return False





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
        path.pop()
        return False








