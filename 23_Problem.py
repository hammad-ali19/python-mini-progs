# Problem 23: Find the Length of the Longest Word

# Write a Python function that takes a string of words and returns the length of the longest word 
# in the string.

def length_of_longest_word (string: str) -> int:
    words: list[str] = string.split()
    longest_word_length: int = len(words[0])
    for i in range (len(words)):
        if len(words[i]) > longest_word_length:
            longest_word_length = len(words[i])
    return longest_word_length


print(length_of_longest_word("Hi, My name is Hammad Ali"))