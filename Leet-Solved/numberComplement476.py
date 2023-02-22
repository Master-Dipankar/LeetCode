# 476. Number Complement
# The
# complement
# of
# an
# integer is the
# integer
# you
# get
# when
# you
# flip
# all
# the
# 0
# 's to 1'
# s and all
# the
# 1
# 's to 0'
# s in its
# binary
# representation.
#
# For
# example, The
# integer
# 5 is "101" in binary and its
# complement is "010"
# which is the
# integer
# 2.
# Given
# an
# integer
# num,
# return its
# complement.
#
# Example
# 1:
#
# Input: num = 5
# Output: 2
# Explanation: The
# binary
# representation
# of
# 5 is 101(no
# leading
# zero
# bits), and its
# complement is 010.
# So
# you
# need
# to
# output
# 2.
# Example
# 2:
#
# Input: num = 1
# Output: 0
# Explanation: The
# binary
# representation
# of
# 1 is 1(no
# leading
# zero
# bits), and its
# complement is 0.
# So
# you
# need
# to
# output
# 0.

class Solution:
    def findComplement(self, num):
        binary = bin(num)[2:]  # i converted the integer to binary and remove the '0b' prefix.

        # here i fliped each character in the binary string with if-eles.
        flipped_binary = ""
        for char in binary:
            if char == '0':
                flipped_binary += '1'
            else:
                flipped_binary += '0'

        # here i have converted the flipped binary string to an integer and return it.
        return int(flipped_binary, 2)


solution = Solution()
num = 5
result = solution.findComplement(num)
print(result)
