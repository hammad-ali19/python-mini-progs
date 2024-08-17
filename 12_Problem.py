# Problem 12: Anagram Check

# Write a Python function that checks whether two given strings are anagrams of each 
# other. An anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once.

def is_anagram (s1: str, s2: str) -> bool:
    flag: bool = True
    for char in s1:
        if char not in s2:
            flag = False
    return flag
    

s1 = "claimed"
s2 = "decimal"

print(is_anagram(s1, s2))   # Output: True


