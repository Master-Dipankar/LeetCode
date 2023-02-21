# 349.
# Intersection
# of
# Two
# Arrays
# Given
# two
# integer
# arrays
# nums1 and nums2,
# return an
# array
# of
# their
# intersection.Each
# element in the
# result
# must
# be
# unique, and you
# may
# return the
# result in any
# order.
#
# Example
# 1:
#
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]
# Example
# 2:
#
# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]
# Explanation: [4, 9] is also
# accepted.
class Solution:
    def intersection(self, nums1, nums2):
        # here i convered num1 and num2 to set which will remove the duplicates

        set1 = set(nums1)

        set2 = set(nums2)

        # here I take the intersection of two sets with the "&" operator and returned it as a list.
        return list(set1 & set2)


solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = solution.intersection(nums1, nums2)
print(result)
