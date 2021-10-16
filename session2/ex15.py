"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""
string = input()
vocale = 'aeiou'
count = 0

for i in vocale:
    for j in string:
        if i == j:
            count += 1
            print(count)
