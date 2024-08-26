# Problem 35: Find the Most Frequent Element in a List
# Write a Python function that takes a list of elements and returns the element
# that appears most frequently. If there are multiple elements with the same frequency, return any one of them.

def count_occurences (List, num):
    length = len(List)
    count = 0
    for i in range(length):
        if List[i] == num:
            count += 1
    return count


def find_frequent_element (List):
    length = len(List)
    frequent_element: int
    max_of_occuences = 0
    for i in range (length):
        current_elm_occurences = count_occurences(List, List[i])

        if max_of_occuences < current_elm_occurences:
            max_of_occuences = current_elm_occurences
            frequent_element = List[i]
    return frequent_element



List = [1, 3, 2, 1, 4, 1, 2, 3, 2, 2, 4, 4, 4, 4]
print(find_frequent_element(List))  # Output: 4