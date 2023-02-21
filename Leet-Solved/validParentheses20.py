# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false

class Solution:
    @staticmethod
    def isValid():
        s = input("Enter a string: ")
        stack = []
        map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in map:
                tp_el = stack.pop() if stack else '#'
                if map[char] != tp_el:
                    return False
            else:
                stack.append(char)

        return not stack


r = Solution.isValid()

print(r)