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



def test_good_guess_input():
    secret_word = "elephant"
    guesses = list('ephqan')
    turns_left = 5
    new_letter = "l"
    assert hangman.turns(new_letter, guesses, turns_left, secret_word)==(turns_left ,guesses+['l', ], hangman.CORRECT_LETTER)

def test_game_lost():
    secret_word = "banana"
    guesses = list('vewopq')
    turns_left = 0
    new_letter = "p"
    assert hangman.turns(new_letter, guesses, turns_left, secret_word) == (turns_left, guesses, hangman.GAME_LOST)   

def test_game_won():
    secret_word = "acid"
    guesses = list('aci')
    turns_left = 7
    new_letter = "d"
    assert hangman.turns(new_letter, guesses, turns_left, secret_word) == (turns_left, guesses, hangman.GAME_WON)

def test_bad_guess_input():
    secret_word = "car"
    guesses = list('ra')
    turns_left = 7
    new_letter = "y"
    assert hangman.turns(new_letter, guesses, turns_left, secret_word) == (turns_left-1, guesses +[new_letter], hangman.WRONG_LETTER)

def test_already_guessed_letter():
    secret_word = "car"
    guesses = list('rax')
    turns_left = 6
    new_letter = "r"
    assert hangman.turns(new_letter, guesses, turns_left, secret_word) == (turns_left, guesses, hangman.ALREADY_GUESSED_LETTER)


def test_display_board_when_won():
    secret_word = 'amazon'
    guesses = ['amzo']
    turns_left = 7
    result = hangman.GAME_WON    
    result_for_display =  """
        


                                    _______YOU_WON!!!_______
                                    The word is amazon


                        
        
        """
    assert hangman.display_board(turns_left, secret_word, guesses, result)== result_for_display


def test_display_board_when_lost():
    secret_word = 'amazon'
    guesses = ['aqwert']
    turns_left = 0
    result = hangman.GAME_LOST
    result_for_display = """



                                    ________YOU LOST!!!_______
                                    The word is amazon
        
        
        
        """
    assert hangman.display_board(turns_left, secret_word, guesses, result)== result_for_display

def test_display_board_when_worng_letter():
    secret_word = 'amazon'
    guesses = ['aqwer']
    turns_left = 1
    result = hangman.WRONG_LETTER
    result_for_display = "You entered a wrong letter\n"
    assert hangman.display_board(turns_left, secret_word, guesses, result)== result_for_display