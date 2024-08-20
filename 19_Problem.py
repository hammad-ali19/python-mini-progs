# Problem 20: Check for Pangram

# Write a Python function that checks whether a given sentence is a pangram. A pangram is a 
# sentence that contains every letter of the alphabet at least once.



def is_pangram (st: str):
    flag = True
    if not st:
        return "Empty string"
    alphabets: list[str] = list(map(chr, range(97, 123)))
    lower_case_string: list[str] = st.lower()
    for ch in alphabets:
        if ch not in lower_case_string:
            flag = False  
            return flag
    return flag
    

print("This program checks if the given string is Pangram or Not.")
s = input("Input: ")
print(f"Output: {is_pangram(s)}")