class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #l = len(nums)
        if k <= 1:
            return 0
        ans = start = 0
        p = 1
        for i, val in enumerate(nums):
            p *= nums[i]
            while p >= k:
                p = p/nums[start]
                start +=1
            ans += i-start+ 1
        return int(ans)
            
            
        '''l = len(nums)
        if k <= 1:
            return 0
        end = 0
        ans = 0
        temp = 0
        for i in range(l):
            p = 1
            while end < l and p*nums[end] < k:
                p = p*nums[end]
                end +=1
            ans += (end - i)* (end - i + 1) / 2
            ans -= (temp - i ) * ( temp - i + 1 ) / 2
            temp = end
            if end == l:
                break
            end = i+1
        return int(ans)'''
