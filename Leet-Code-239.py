class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if k == 1:
            return nums
        r = []
        for i in range(len(nums) - k+1):
            r.append(max(nums[i:i+k]))
        return r
