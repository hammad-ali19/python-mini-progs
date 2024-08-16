# Problem 7: Fibonacci Sequence
# Write a Python function that generates the first n numbers in the 
# Fibonacci sequence. The Fibonacci sequence is a series of numbers where 
# the next number is found by adding up the two numbers before it, starting 
# with 0 and 1

def fibonacci_seq (number: int) -> None:
    a: int = 0
    b: int = 1
    temp: int = 0
    for i in range (number):
        print(a, end=" ")
        # a, b = b, a + b  Can also be done in single statement without using temp variable
        temp = a
        a = b
        b = temp + a


fibonacci_seq(5)