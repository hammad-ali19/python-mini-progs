# Problen 27: Count the Occurrences of a Character in String

# Write a Python function that takes a string and a character as input and returns the number of times that
# character appears in the string.

def count_occurrences_of_char (string: str, char: chr) -> int:
    counter: int = 0
    for c in string:
        if c == char:
            counter += 1
    return counter


print(count_occurrences_of_char("banana", 'a'))