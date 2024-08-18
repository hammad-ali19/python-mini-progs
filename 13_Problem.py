# Problem 13: Capitalize Words

# Write a Python function that takes a sentence and returns the sentence with each 
# word capitalized.

def capitalize (string: str) -> str:
    s = string.title()
    return s


string = "hello world"
s = capitalize(string)
print(s)