# Problem 24: Remove Punctuation from a String

# Write a Python function that removes all punctuation marks from a given string.

def remove_punctuation (string: str) -> str:
    new_string: str = ""
    alphabets: list[chr] = list(map(chr, range(65, 123)))
    alphabets.append(" ")
    for char in string:
        if char not in alphabets:
            continue
        else:
            new_string += char
    return new_string


print(remove_punctuation("Hi, My name is Hammad Ali!"))
