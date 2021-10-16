"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
string = input()

string_nou = ""
i = 0

for x in string:
    if i % 2 == 0:
        string_nou = string_nou + string[i].upper()
        i += 1
    else:
        string_nou = string_nou + string[i].lower()
        i += 1

print(string_nou)
