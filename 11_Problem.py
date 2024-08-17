# Problem 11: Merge and Sort Lists

# Write a Python function that takes two lists of numbers and returns a 
# single sorted list that merges both lists.

def mergeANDsort (list1: int, list2: int) -> list[int]:
    merged_list: list[int] = list1 + list2
    merged_list.sort()
    return merged_list


first: list[int] = [3, 7, 9, 10]
second: list[int] = [1, 2, 5]
sorted = mergeANDsort(first, second)
print(sorted) # Output: [1, 2, 3, 5, 7, 9, 10]