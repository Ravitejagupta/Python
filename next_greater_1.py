class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for i in findNums:
            if nums.index(i) == len(nums) - 1:
                r.append(-1)
            else:
                dummy = nums[nums.index(i)+1:]
                for j in range(len(dummy)):
                    if dummy[j] > i:
                        r.append(dummy[j])
                        break
                else:
                    r.append(-1)
        return r
