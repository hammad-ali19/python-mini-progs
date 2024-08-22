# Problem 28: Find the Median

# Write a Python function that takes a list of numbers and returns the median. The median is the middle value
# in a list when the numbers are sorted. If the list has an even number of elements, the median is the 
# average of the two middle numbers.


def calc_median (list: int) -> int:
    median: int = 0
    length = len(list)
    if (length % 2) == 0:
        length = length // 2
        median = (list[length] + list[length - 1]) / 2
        return median
    else:
        return list[length // 2]
    

print (calc_median([1, 2, 3, 4, 5, 6, 8, 9]))