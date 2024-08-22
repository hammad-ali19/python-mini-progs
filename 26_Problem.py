# Problem 26: Find the Intersection of Two Lists

# Write a Python function that takes two lists and returns a list that contains only the elements that are
# common to both lists.

def commons_in_lists (list1, list2):
    common_items: list = []
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items


list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
common_items = commons_in_lists(list_1, list_2)
print(common_items)