class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        b = [False]* len(nums)
        for i in range(len(nums)):
            s,c = nums[i],0
            while(not b[s]):
                temp = s
                s = nums[s]
                c+=1
                b[temp] = True
            r = max(r,c)
        return r
