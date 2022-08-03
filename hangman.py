import random

def get_random_word(path="/usr/share/dict/words"):
    file_for_random_word = open(path, "r").readlines()
    while 1:
        random_word = random.choice(file_for_random_word).strip()
        if len(random_word)>=6 and random_word.isalpha() and not random_word[0].isupper():
            # print(random_word)
            return random_word
            
    

print(get_random_word())