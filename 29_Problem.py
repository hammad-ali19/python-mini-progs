# Problem 29: Generate a List of Prime Numbers
# Write a Python function that takes an integer n and returns a list
# of all prime numbers up to n. This problem will help you practice
# generating sequences and understanding prime number properties.


def generate_prime_numbers_upto (num: int):
    for i in range (2, num+1):
        for j in range (2, i):
            if i % j == 0:
                break
        else:
            yield i


print("""
This Program generates list of prime number upto the 
given number...\n""")
num = int(input("Input: "))
gen = generate_prime_numbers_upto(num)
prime_numbers: list[int] = []

for j in gen:
    prime_numbers.append(j)
    
print(f"Output: {prime_numbers}")
