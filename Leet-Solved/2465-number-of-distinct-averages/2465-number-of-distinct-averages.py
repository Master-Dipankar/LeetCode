class Solution:
    def distinctAverages(self, nums):
        averages = set()
        while nums:
            min_num = min(nums)
            nums.remove(min_num)
            max_num = max(nums)
            nums.remove(max_num)
            avg = (min_num + max_num) / 2.0
            averages.add(avg)
        return len(averages)
