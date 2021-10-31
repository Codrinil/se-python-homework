"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""


def log_output(func):
    with open('output11.data', 'a') as file:
        file.write(func())
        file.close()

# decorate me


@log_output
def f():
    return "CMI"


f()
