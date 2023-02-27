from typing import List

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n

        # Compute the prefix sum of nums
        for i in range(1, n):
            left_sum[i] = left_sum[i-1] + nums[i-1]

        # Compute the suffix sum of nums
        for i in range(n-2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i+1]

        # Compute the absolute difference
        answer = [abs(left_sum[i] - right_sum[i]) for i in range(n)]

        return answer
