# Problem 14: Sum of Digits

# Write a Python function that takes a positive integer and returns the sum of its 
# digits.

def sum_of_digits (number: int) -> int:
    sum: int = 0
    while (number != 0):
        digit = number % 10
        number //= 10
        sum += digit
    return sum


print(sum_of_digits(124091))