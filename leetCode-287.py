class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set()
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                return i
