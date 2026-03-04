#Project No.2#
#Authors: Grace DeGroot and Garrett Stroud
#Description: Main function that allows the user to enter a seed and word, and generates them a boggle board based on the seed.
#The user can enter a desired word, and it is checked for correctness. It also checks for if the word is a palindrone.

#Imports the file with the board class.
import BoggleBoard

#Main function
def main():
    #Has the user enter the seed, and intilizes the board, filling and printing it.
    seed = input('Enter seed: ')
    board = BoggleBoard.BoggleBoard(seed)
    board.fill_board()
    board.print_board()

    #Allows the user to enter a word.
    word = 'Enter word (in UPPERcase): '
    path = board.check_board(word)

    #Checks if the word is on the board, and if it is a palindrone, prints corresponding message.
    if board.check_board():
        print('Nice Job!')
        check_palindrome(word)
        board.print_highlihted()
        
    else:
        print(f"I don't see that word.")
        if not check_palindrome(word):
            print('Are we looking at the same board?')
    

#Palindrome function, checks if given word is a palindrome
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

#Prints message if word is or isn't a palindrome.
def check_palindrome(word):
    if is_palindrome(word):
            print(f'The word {word} is a palindrome.') 
    else:
        print(f'The word {word} is not a palindrome.', end = " ")

#Call to the main function.
main()
