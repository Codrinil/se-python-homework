"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""


# my_str = 'aabbcc'
# rep_str = ''
# for letter in my_str:
#     code = ord(letter)
#     nxt_letter = chr(code+1)
#     rep_str += nxt_letter


# print(rep_str)

def upper_letter(my_str=input()):
    rep_str = ''
    for letter in my_str:
        # code = ord(letter)
        nxt_letter = chr(ord(letter)+1)
        rep_str += nxt_letter
    return rep_str


print(upper_letter())
