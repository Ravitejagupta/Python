class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 1
        for i in range(0,len(nums)-1,2):
            if nums[i+1] != nums[i]:
                return nums[i]
        return(nums[-1])
