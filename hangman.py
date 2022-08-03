import string
import random

def get_random_word():
    file_for_random_word = open("/usr/share/dict/words","r").readlines()
    while 1:
        random_word = random.choice(file_for_random_word).strip()
        if len(random_word)>=6:
            print(random_word)
            break

get_random_word()