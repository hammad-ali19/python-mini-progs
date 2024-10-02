# Problem 38: Find the Longest Palindromic Substring
# Write a Python function that takes a string and returns the longest palindromic substring. A palindromic 
# substring is a sequence that reads the same backward as forward.


def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    if len(s) == 0:
        return ""
    
    longest = ""
    
    for i in range(len(s)):
        # Check for odd-length palindromes
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Check for even-length palindromes
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest


# Test cases
print(longest_palindromic_substring("dabab"))  # Output: "bab" or "aba"
# print(longest_palindromic_substring("cbbd"))   # Output: "bb"
    
