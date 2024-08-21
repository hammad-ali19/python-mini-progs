# Problem 21: Sum of Even Numbers in a List

# Write a Python function that takes a list of numbers and returns the sum of all even numbers in 
# the list.

def sum_of_even_numbes (nums: list[int]) -> int:
    if not nums:
        return "List was Empty! "
    sum: int = 0
    for i in range (len(nums)+1):
        if (i % 2) == 0:
            sum += i
    return sum


print(sum_of_even_numbes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))