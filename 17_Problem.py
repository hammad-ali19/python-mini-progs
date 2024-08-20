# Problem 17: Find the GCD (Greatest Common Divisor)

# Write a Python function that takes two integers and returns their greatest common divisor 
# (GCD). The GCD is the largest positive integer that divides both numbers without leaving a 
# remainder.


def GCD (num1, num2):
    com_divisors = []
    minimum = min(num1, num2)
    for i in range(2, minimum):
        if ((num1 % i) == 0) and ((num2 % i) == 0):
            com_divisors.append(i)
    if not com_divisors:
        return ("No common divisors")
    return max(com_divisors)


print(GCD(42, 98))

