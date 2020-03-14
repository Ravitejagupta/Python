class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        m1 = m2 = m3 = -sys.maxsize - 1
        for num in nums:
            if num > m1:
                m3 = m2
                m2 = m1
                m1 = num
            elif num in range(m2,m1):
                m3 = m2
                m2 = num
            elif num > m3:
                m3 = num
        return m3
