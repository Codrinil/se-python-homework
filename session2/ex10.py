"""
    Ex. 10: Modificati urmatoarea bucata de cod astfel incat
    la rulare, sa printati dictionarul d1 care va avea ca si chei elementele
    din l1 iar ca valori, elementele din l2

    Raspunsul corect la printare arata asa:
    {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd'
    }
"""

# In variabila l1 si l2 avem urmtoarele liste:
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']

# In varaibila d1 avem un dictionar gol
d1 = {}

# # Afisam listele l1 si l2
# print(d1)
d1 = dict(zip(l1, l2))
print(d1)

for key in l1:
    for value in l2:
        d1[key] = value
        l2.remove(value)
        break
print(d1)
