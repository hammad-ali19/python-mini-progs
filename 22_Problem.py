# Check for Prime Number

# Write a Python function that checks whether a given integer is a prime number. A prime number 
# is a number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime_number (number: int) -> bool:
    is_prime: bool
    for i in range (2, number):
            if number % i == 0:
                is_prime = False
                return is_prime
    else:
        is_prime = True
        return is_prime


print(is_prime_number(11))   #Output: True