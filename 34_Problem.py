# Problem 34: Rotate a List
# Write a Python function that takes a list and an integer k as input and returns the list rotated to the right by k positions.

def rotate_list (List, k):

    length = len(List)
    rotated_list: list = []

    for i in range(k):
        rotated_list.append(List[length-k])
        k -= 1
    length -= len(rotated_list)

    for i in range (length):
        rotated_list.append(List[i])
    return rotated_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotated_list = rotate_list(my_list, 4)

print(rotated_list) # Output: [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]