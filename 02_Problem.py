# Write a Python function that takes a list of numbers and returns the largest 
# number in the list.

def largest_number (numbers: list[int]) -> int:
        if len(numbers) == 0:
            return -1
        else:
            largest: int = numbers[0]
            for num in numbers:
                if num > largest:
                    largest = num
            return largest
    


nums: list[int] = []
maximum: int = largest_number(nums)
if maximum == -1:
    print("List was Empty")
else:
    print(f"Largest number: {maximum}")