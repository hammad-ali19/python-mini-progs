# Problem 8: Find Prime Numbers
# Write a Python function that takes an integer n and returns a list of all prime numbers less 
# than or equal to n. A prime number is a number greater than 1 that has no positive divisors 
# other than 1 and itself.


def check_prime(number: int) -> bool:
    is_prime = True
    for i in range (number):
        if i == 0 or i == 1:
            continue
        else:
            if number % i == 0:
                is_prime = False
                break
    return is_prime


def list_of_prime_numbers_upto (number: int) -> list[int]:
    prime_numbers: list[int] = []
    for n in range(number+1):
        if n == 0 or n == 1:
            continue
        elif check_prime(n):
            prime_numbers.append(n)
    return prime_numbers


number: int = 61
prime_numbers = list_of_prime_numbers_upto(number)
print(prime_numbers)