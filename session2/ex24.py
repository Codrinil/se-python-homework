"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""
n = int(input())
numar_introdus = n
numar_intors = 0
while(n > 0):
    ultima_cifra = n % 10
    numar_intors = numar_intors * 10 + ultima_cifra
    n = n//10
print(numar_introdus == numar_intors)
