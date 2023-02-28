'''To merge the two arrays in non-decreasing order, we can use a two-pointer approach. We start with two pointers, one at the end of nums1 and the other at the end of nums2. We compare the elements at these pointers and place the larger element at the end of nums1. We then move the corresponding pointer back one position. We repeat this process until we have merged all the elements from nums2 into nums1 in non-decreasing order.

# Since we are overwriting the elements of nums1 from the end, we need to start from the end of the merged array and move backwards. At each step, we compare the elements at the two pointers and place the larger element at the end of the merged array. '''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1 # pointer for nums1
        j = n - 1 # pointer for nums2
        k = m + n - 1 # pointer for merged array

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # if there are any remaining elements in nums2
        # that have not been merged, add them to the beginning of nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
            
'''I start with three pointers, i, j, and k. Pointer i points to the last element of nums1, pointer j points to the last element of nums2, and pointer k points to the last element of the merged array.

I then loop while both pointers i and j are valid, i.e., i >= 0 and j >= 0. At each step, I compare the elements at nums1[i] and nums2[j]. If nums1[i] is larger, I place it at the end of the merged array, nums1[k]. Otherwise, I place nums2[j] at nums1[k]. I then move the corresponding pointer back one position and repeat the process.

If there are any remaining elements in nums2 that have not been merged, I add them to the beginning of nums1. I do this by looping while pointer j is still valid, and adding the remaining elements at nums2[j] to the beginning of nums1, starting from the first position.

Finally, I don't need to return anything since I have modified nums1 in place.
'''




        