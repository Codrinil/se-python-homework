"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa printati True (boolean) de fiecare data cand elementul
    primit este par, si False (boolean) de fiecare data cand elemtnul primit
    este impar.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa:
        False
        False
        True
        False
        False
"""


# while True:
#     comanda = input('>')
#     numar = int(input(''))
#     print(numar)
#     if comanda.lower() == 'exit':
#         break
# print(bool(numar % 2 == 0))
# command = ''
# numar = int(input())
# while command.lower() != 'exit':
#     command = input()
#     print(bool(numar % 2 == 0))

comanda = input().split(',')

for x in comanda:
    if x != 'exit':
        if int(x) % 2 == 0:
            print('True')
        else:
            print('False')
