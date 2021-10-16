# """
#     Veti primi un string de la tastatura.
#     Va trebui sa printati numarul de vocale si numarul de consoane din
#     acel string.

#     exemplu:
#         Veti primi: 'center'
#         Veti printa:
#         2 (pentru vocale)
#         4 (pentru consoane)
# """

##

string = 'center'
for x in string:
    if x in 'aeiou':
        x = 2
    else:
        x = 4
    l1 = x
    print(l1)
