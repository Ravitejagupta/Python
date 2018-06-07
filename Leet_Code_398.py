class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        d = {}
        for index,val in enumerate(self.nums):
            if val in d:
                d[val].append(index)
            else:
                d[val] = [index]
        l = len(d[target])
        return d[target][random.randint(0,l-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
