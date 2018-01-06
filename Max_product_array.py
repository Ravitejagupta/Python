class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def product(i,j):
            p = 1
            for k in range(i,j+1):
                p=p*nums[k]
            return p
        M = [[0 for i in nums] for i in nums]
        for i in range(len(nums)):
            p = product(0,i)
            for j in range(i,len(nums)):
                if i==0:
                    M[j][j] = nums[j]
                else:
                    M[j-i][j] = max(M[j-i][j-1], M[j-i+1][j],product(j-i,j))
        print(M)
        return (M[0][len(nums)-1])
        
        #O(n^2)
