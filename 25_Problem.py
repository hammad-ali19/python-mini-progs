# Problem 25: Calculate the Average of a List

# Write a Python function that takes a list of numbers and returns the average of those numbers.

def calc_avg (numbers: list[int]) -> float:
    sum: int = 0
    avg: float = 0.0
    for num in numbers:
        sum += num
    avg = sum / len(numbers)
    return avg


print(calc_avg([10, 20, 30, 40]))    # Output: 25.0