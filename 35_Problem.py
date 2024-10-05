# Problem 35: Merge Two Sorted Lists
# Write a Python function that takes two sorted lists and merges them into a single sorted list 
# without using any built-in sort functions.


def find_minimum (List, start=0):
    mini_idx = start
    length = len(List)
    for i in range (start, length):
        if List[i] < List[mini_idx]:
            mini_idx = i
    return mini_idx


def sort_list (List):
    for i in range (len(List)):
        mini_ind = find_minimum(List, i)
        temp = List[i]
        List[i] = List[mini_ind]
        List[mini_ind] = temp
    return List


def mergeANDsort (l1, l2):
    List = l1 + l2
    List = sort_list(List)
    return List


L1 = [3, 5, 7]
L2 = [2, 4, 6]
print(mergeANDsort(L1, L2))