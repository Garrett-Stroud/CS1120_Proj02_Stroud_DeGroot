#Project No.2#




import BoggleBoard

def main():
    seed = input('Enter seed: ')
    board = BoggleBoard.BoggleBoard(seed)
    board.fill_board()
    board.print_board()

    word = 'Enter word (in UPPERcase): '

    if board.check_board():
        print('Nice Job!')
        check_palindrome(word)
        board.print_highlihted()
        
    else:
        print(f"I don't see that word.")
        if not check_palindrome(word):
            print('Are we looking at the same board?')
    


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

def check_palindrome(word):
    if is_palindrome(word):
            print(f'The word {word} is a palindrome.') 
    else:
        print(f'The word {word} is not a palindrome.', end = " ")

main()
