# Problem 18: Flatten a List
# Write a Python function that takes a list of lists (nested list) and returns a single 
# flattened list.

def flattened_list (nested_list):
    if not nested_list:
        return "List was empty"
    fl_list = []
    length = len(nested_list)
    for i in range (length):
        fl_list += nested_list[i]
    return fl_list


print (flattened_list([[1,2],[3,4],[5,6],[7,8],[9,10]]))
