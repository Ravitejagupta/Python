class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        r = []
        ans1 = ans2 = -1
        while left <= right:
            mid = left + (right-left)//2
            print(mid)
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                ans1 = ans2 = mid
                break
        if ans1 == -1 or ans2 == -1:
            return [-1,-1]
        while ans1 >= 0:
            if nums[ans1] == target:
                ans1 -= 1
            else:
                break
        r.append(ans1+1)
        while ans2 < len(nums):
            if nums[ans2] == target:
                ans2 += 1
            else:
                break
        r.append(ans2 -1)
        return r
