"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""

# numbers = [1, 2, 3, 4]

# # Each function call represents an elf doing his work


# def sum_elements(numbers):
#     total = 0
#     # Worker elf doing his work
#     if len(numbers) == 1:
#         total += int(numbers[0])
#         print("Adding the number", total)

#     # Manager elf doing his work
#     else:
#         mid = len(numbers) // 2
#         first_half = numbers[:mid]
#         second_half = numbers[mid:]

#         # Divides his work among two elves
#         sum_elements(first_half)
#         sum_elements(second_half)
#     return total

def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)


print(list_sum_recursive([1, 2, 3, 4]))
