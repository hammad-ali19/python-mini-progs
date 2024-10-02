# Problem 39: Calculate the nth Fibonacci Number (Using Dynamic Programming)
# Write a Python function that takes an integer n and returns the nth Fibonacci number. Use dynamic programming to optimize the solution.



def nth_fib_number (number):
    pass


def fibonacci_seq (number: int):
    nth_num = 0
    a: int = 0
    b: int = 1
    temp: int = 0
    for i in range (number):
        # print(a, end=" ") 
        nth_num = a
        # a, b = b, a + b  Can also be done in single statement without using temp variable
        temp = a
        a = b
        b = temp + a
    return nth_num


print(fibonacci_seq(11))