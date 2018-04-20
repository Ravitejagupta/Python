class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
        
        
        
        #solution2 - O(n)
        '''if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        m1, m3 = max(nums[0:3]),min(nums[0:3])
        if nums[0] != m1 and nums[0] != m3:
            m2 = nums[0]
        elif nums[1] != m1 and nums[1] != m3:
            m2 = nums[1]
        else:
            m2 = nums[2]
        #print(m1,m2,m3)
        if nums[0] > nums[1]:
            min1 = nums[1]
            min2 = nums[0]
        else:
            min1,min2 = nums[0],nums[1]
        for i in nums[3:]:
            if i > m3:
                if i > m1:
                    m3 = m2
                    m2 = m1
                    m1 = i
                elif i > m2:
                    m1, m2 = m2, i
                else:
                    m3 = i
            if i < min2:
                if i < min1:
                    min2,min1 = min1, i
                else:
                    min2 = i
        print(m1,m2,m3,min1,min2)
        return max(m1*m2*m3, min1*min2*m1)
                '''
                
