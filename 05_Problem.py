# Problem 5: Reverse a String
# Write a Python function that takes a string as input and returns the string in 
# reverse order.

# String: str = "python"
# reversed_String: str = String[::-1] Built-in way for reversing a string
# print(reversed_String)

def reverse_string (string: str) -> str:
    reversed_string: str = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string
    

fav_lang: str = "Python"
print(reverse_string(fav_lang))
