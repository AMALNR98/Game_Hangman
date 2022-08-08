ALREADY_GUESSED_LETTER = 1
WRONG_LETTER = 2
CORRECT_LETTER = 3
GAME_LOST=6
GAME_WON = 7
START_GAME = 9
import random
from readline import get_completer_delims

def get_random_word(path="/usr/share/dict/words"):
    '''To get a random word from dictionary'''
    file_for_random_word = open(path).readlines()
    while 1:
        random_word = random.choice(file_for_random_word).strip()
        if len(random_word)>=6 and random_word.isalpha() and not random_word[0].isupper():
            return random_word
            
    
def mask_word(random_word, guesses):
    
    hidden_word = ''
    for char in random_word:
        if char in guesses:
            hidden_word += char
        else:
            hidden_word += '-'
    return hidden_word

def turns(new_letter, secret_word, guesses, turns_left):
    if turns_left == 1:
        return turns_left, guesses, GAME_LOST
    if new_letter in guesses:
        return turns_left, guesses, ALREADY_GUESSED_LETTER
    if secret_word == mask_word(secret_word, guesses +[new_letter, ]):
        return turns_left, new_letter, GAME_WON

    guesses = guesses +[new_letter, ] 

    if new_letter not in secret_word:
        turns_left -= 1
        display = WRONG_LETTER
    else:
        display = CORRECT_LETTER
    return turns_left, guesses,display

def display_board(turns_left, secret_word, guesses, result):
    print(guesses)  
    result_for_display = f"""guess: {" ".join(guesses)}
        {mask_word(secret_word, guesses)}
        turns_left: {turns_left}""" 
    
    if result ==START_GAME:
        result_for_display="enter the guess"
    if result == CORRECT_LETTER:
        result_for_display ="You entered correct letter\n"
        return result_for_display
    if result == ALREADY_GUESSED_LETTER:
        result_for_display="you already guessed that letter\n"
        return result_for_display
    if result == GAME_WON:
        return f"""YOU_WON!!!
        The word is {secret_word}"""
    else:
        return f"""YOU LOST!!!
        The word is {secret_word}"""

def main():
    turns_left = 7 
    secret_word = get_random_word()
    guesses = []
    print(secret_word)
    result= START_GAME
    while 1:
        print(display_board(turns_left=turns_left, secret_word=secret_word, guesses=guesses, result=result))
        new_letter = input("guess a letter:")
        turns_left, guesses, result = display_board(new_letter, guesses, turns_left, result)

        if result == GAME_WON:
            print(display_board(turns_left, secret_word, guesses, result))
            break
        if result ==GAME_LOST:
            print(display_board(turns_left, secret_word, guesses, result))
            break

if __name__ == "__main__":
    main()
