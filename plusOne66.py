# 66.
# Plus
# One

# You
# are
# given
# a
# large
# integer
# represented as an
# integer
# array
# digits, where
# each
# digits[i] is the
# ith
# digit
# of
# the
# integer.The
# digits
# are
# ordered
# from most significant
#
# to
# least
# significant in left - to - right
# order.The
# large
# integer
# does
# not contain
# any
# leading
# 0
# 's.
#
# Increment
# the
# large
# integer
# by
# one and
# return the
# resulting
# array
# of
# digits.
#
# Example
# 1:
#
# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]
# Explanation: The
# array
# represents
# the
# integer
# 123.
# Incrementing
# by
# one
# gives
# 123 + 1 = 124.
# Thus, the
# result
# should
# be[1, 2, 4].
# Example
# 2:
#
# Input: digits = [4, 3, 2, 1]
# Output: [4, 3, 2, 2]
# Explanation: The
# array
# represents
# the
# integer
# 4321.
# Incrementing
# by
# one
# gives
# 4321 + 1 = 4322.
# Thus, the
# result
# should
# be[4, 3, 2, 2].
# Example
# 3:
#
# Input: digits = [9]
# Output: [1, 0]
# Explanation: The
# array
# represents
# the
# integer
# 9.
# Incrementing
# by
# one
# gives
# 9 + 1 = 10.
# Thus, the
# result
# should
# be[1, 0].
class Solution:
    def plusOne(self, digits):
        # Convert the array of digits ie[1,2,3] to an integer 123
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]

        # Increment the integer by one ie 123+1=124
        num += 1

        # Convert the integer back to an array of digits ie converting 124 to [1,2,4]
        result = []
        while num > 0:
            result.insert(0, num % 10)
            num //= 10

        return result if result else [0]


solution = Solution()
digits = [1, 2, 6]
result = solution.plusOne(digits)
print(result)
