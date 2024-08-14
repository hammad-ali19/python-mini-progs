# Problem 1: Sum of Numbers
# Write a Python function that takes a list of numbers as input and returns 
# the sum of those numbers.

def sum_of_numbers(numbers: list[int]) -> int:
    if not numbers:
        return -1
    else:
        sum: int = 0
        for number in numbers:
            sum = sum + number
        return sum
        
        

nums: list[int]= []
Sum: int = sum_of_numbers(nums)
if Sum == -1:
    print("List was Empty! ")
else:
    print(f"Sum is {Sum}.")