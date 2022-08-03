from itertools import groupby
from operator import itemgetter

word_list = ['ball','has','did','say','got','made','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','sim','felt','live','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)