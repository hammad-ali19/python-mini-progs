# Problem 34: Check for Armstrong Number

# Write a Python function that checks whether a given integer
# is an Armstrong number. An Armstrong number (also known as
# anarcissistic number) is a number that is equal to the sum of 
# its own digits each raised to the power of the number of digits.


def is_armstrong_number (number: str) -> int:
    if number.isdigit():
        sum = 0
        length = len(number)
        for i in range(length):
            sum += int(number[i])**length
        if sum == int(number):
            return True
        else:
            return False
    else:
        return ("Invalid Input! ")


num = input("Input: ")
print(f"Output: {is_armstrong_number(num)}")



