from multiprocessing.context import assert_spawning
from re import L
import hangman
import random
random.seed(10)

def test_get_random_word_min_length_6():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['ambulances', 'cat', 'car', 'dog', "hen"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "ambulances"

def test_get_random_word_no_non_alphanum():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['elephants', "hospital's", "policeman's"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "elephants"

def test_get_random_word_no_proper_noun():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['firehouse', "Abraham", "Mercury"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "firehouse"


def test_get_random_word():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['ambulances', 'hospitalized', 'car', 'Abraham', "mercury's"]:
            f.write(i+"\n")
    words = set()
    for _ in range(10):
        word = hangman.get_random_word(my_dict)
        print (word)
        words.add(word)
    assert words == {"hospitalized", 'ambulances'}

# RED - Implement a test that will fail
# GREEN - Make the test pass
# REFACTOR - Adjust the code so that all tests pass and code is improved


def test_mask_word_no_guesses():
    for i in ["police", "elephant", "it", "foo"]:
        assert hangman.mask_word(i, []) == len(i)*"-"

def test_mask_word_invalid_guesses():
    for i in ["police", "elephant", "it", "foo" ,"cannon"]:
        assert hangman.mask_word(i, ["x", "q"]) == len(i)*"-"


def test_mask_word_single_guesses():
    assert hangman.mask_word('police',['e'])=='-----e'
    assert hangman.mask_word('police',['a','i','p'])=='p--i--'

def test_mask_word_multiple_guesses():
    assert hangman.mask_word('cannon',['n']) == '--nn-n'

def test_mask_word_with_no_single_gusses():
    assert hangman.mask_word('police',['z'])=='------'



def test_good_geuss_input():
    secret_word = "elephant"
    guesses = list('ephan')
    turns_left = 5
    new_letter = "l"
    assert hangman.turns(new_letter,secret_word,guesses,turns_left)==(turns_left ,guesses+['l', ], hangman.CORRECT_LETTER)

def test_game_lost():
    secret_word = "banana"
    guesses = list('cblknr')
    turns_left = 1
    new_letter = "l"
    assert hangman.turns(new_letter, secret_word, guesses, turns_left) == (turns_left, guesses, hangman.GAME_LOST)   

def test_game_won():
    secret_word = "banana"
    guesses = list('bnx')
    turns_left = 6
    new_letter = "a"
    assert hangman.turns(new_letter, secret_word, guesses, turns_left) == (turns_left, guesses, hangman.GAME_WON)

def bad_guess_input():
    secret_word = "car"
    guesses = list('rax')
    turns_left = 4
    new_letter = "q"
    assert hangman.turns(new_letter, secret_word, guesses, turns_left) == (turns_left - 1, guesses + ['q', ], hangman.WRONG_LETTER)

def already_guessed_letter():
    secret_word = "car"
    guesses = list('rax')
    turns_left = 4
    new_letter = "r"
    assert hangman.turns(new_letter, secret_word, guesses, turns_left) == (turns_left, guesses, hangman.ALREADY_GUESSED_LETTER)



