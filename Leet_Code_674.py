class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        r = [1]*len(nums)
        m = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                r[i] = r[i-1] + 1
                m = max(m,r[i])
        return(m)
