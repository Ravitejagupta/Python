class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        for index,val in enumerate(s):
            if d[val] == 1:
                return index
        return -1
