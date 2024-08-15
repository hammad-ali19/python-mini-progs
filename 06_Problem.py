# Problem 6: Palindrome Check
# Write a Python function that checks whether a given string is a palindrome.

####################### FIRST METHOD #######################

# def reverse_string (string: str) -> str:
#     reversed_string: str = ""
#     for char in string:
#         reversed_string = char + reversed_string
#     return reversed_string

# def is_palindrome (string: str) -> bool:
#     reversed_string: str = reverse_string(string)
#     if string == reversed_string:
#         return True
#     else:
#         return False

####################### SECOND METHOD ########################

def is_palindrome (string: str) -> bool:
    string: str = string.lower()
    flag: bool = True
    length: int = len(string)
    max_iterations: int = length // 2

    for i in range(max_iterations):
        length -= 1
        if string[i] != string[length]:
            flag = False
    return flag
        


string = "Deified"
if_palindrome: bool = is_palindrome(string)
print(if_palindrome)