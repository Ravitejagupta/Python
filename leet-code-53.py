class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        total_max = -2147483647
        for num in nums:
            maximum += num
            total_max = max(total_max, maximum)
            if maximum < 0:
                maximum = 0
        return total_max
