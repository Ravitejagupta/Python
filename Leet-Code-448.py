class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        r = []
        for i in range(1,len(nums) + 1):
            if i not in s:
                r.append(i)
        return r
        
