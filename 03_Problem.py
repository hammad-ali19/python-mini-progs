# Problem 3: Count Vowels
# Write a Python function that counts the number of vowels (a, e, i, o, u) 
# in a given string.

def is_vowel (char: str) -> bool:
    char = char.lower()
    if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
        return False
    else:
        return True
    

def count_vowels (string: str) -> int:
    count: int = 0
    for ch in string:
        if is_vowel(ch):
            count = count + 1
    return count


string: str = "Hi, I am Hammad Ali"
no_of_vowels = count_vowels(string)
print(f"No of Vowels: {no_of_vowels}")

