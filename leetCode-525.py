class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {0:-1}
        ans = 0
        num = 0
        for i,val in enumerate(nums):
            if val == 0:
                num +=1
            else:
                num -= 1
                
            if num in d:
                ans = max(ans, i - d[num])
            else:
                d[num] = i
        print(d)
        return ans
