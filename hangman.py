import string
import random

def get_random_word():
    file_for_random_word = open("/usr/share/dict/words","r").readlines()
    # print(file_for_random_word.read())
    random_word = random.choice(file_for_random_word).strip()
    print(random_word)

get_random_word()