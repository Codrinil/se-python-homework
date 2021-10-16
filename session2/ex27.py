"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""

import random
import string


numar = int(input())
string_aleator = string.ascii_lowercase
print(''.join(random.choice(string_aleator)
              for i in range(numar)))
