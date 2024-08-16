# Problem 9: Remove Duplicates
# Write a Python function that takes a list of numbers and returns a new list with all duplicate 
# numbers removed.


def remove_duplicates (list_of_numbers: list[int]) -> list[int]:
    new_list: list[int] = []
    for i in range(len(list_of_numbers)-1):
        if list_of_numbers[i] not in new_list:
            new_list.append(list_of_numbers[i])
    return new_list


nums: list[int] = [1, 2, 2, 5, 6, 7, 5, 2]
without_duplicates: list[int] = remove_duplicates (nums)
print(without_duplicates)