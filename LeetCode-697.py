class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        d = {}
        degree = 0
        ans = 100000
        for i,val in enumerate(nums):
            if val in d:
                d[val].append(i)
            else:
                d[val] = [i]
        print(d)
        for i in d:
            if len(d[i]) > degree:
                degree = len(d[i])
                ans = max(d[i]) - min(d[i]) + 1
            elif len(d[i]) == degree:
                ans = min(ans, (max(d[i]) - min(d[i]) + 1))
        return ans
