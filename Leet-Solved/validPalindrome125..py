# 125.
# Valid
# Palindrome
# A
# phrase is a
# palindrome if, after
# converting
# all
# uppercase
# letters
# into
# lowercase
# letters and removing
# all
# non - alphanumeric
# characters, it
# reads
# the
# same
# forward and backward.Alphanumeric
# characters
# include
# letters and numbers.
#
# Given
# a
# string
# s,
# return true if it is a
# palindrome, or false
# otherwise.
#
# Example
# 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a
# palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #This line converts the entire string to lowercase to make the comparison case-insensitive.
        s = s.lower()
        #This line initializes two pointers, one pointing to the beginning of the string and one pointing to the end of the string.
        left, right = 0, len(s) - 1
        #This is a loop that continues until the two pointers meet in the middle of the string
        while left < right:
        #These two lines skip over any non-alphanumeric characters at the beginning and end of the string respectively.
            while left < right and not s[left].isalnum(): #isalnum() is a method in Python that checks whether a string consists only of alphanumeric characters returns True if the string contains only alphanumeric characters and False otherwise
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
        # This line checks if the characters at the two pointers are equal. If they are not equal, the string is not a palindrome and the function returns False.
            if s[left] != s[right]:
                return False
        #These two lines move the pointers towards the middle of the string, so the next characters can be compared
            left += 1
            right -= 1
        return True