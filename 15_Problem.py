# Problem 15: Find the Second Largest Number

# Write a Python function that finds the second largest number in a list of numbers.

def second_largest (list_of_numbers: list[int]) -> int:
    list_of_numbers.sort()
    return list_of_numbers[-2]


nums: list[int] = [12, 43, 67, 34, 23, 90]
print(second_largest(nums))