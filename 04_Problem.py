# Problem 4: Factorial of a Number
# Write a Python function that calculates the factorial of a given number n.
# The factorial of n (written as n!) is the product of all positive integers
#  up to n.

def calc_factorial (number: int) -> int:
    if number == 0:
        return 1
    elif number < 0:
        return None
    else:
        fact: int = 1
        for i in range(1, number+1):
            fact = fact * i
        return fact


number: int = 2
fact = calc_factorial(number)
if fact == None:
    print("Factorial of NEGATIVE number cannot be computed! ")
else:
    print(f"The factorial of {number} is {fact}.")