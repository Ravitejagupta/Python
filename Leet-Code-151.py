class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s.split()
        res = ""
        for s in r:
            res = s + " " + res
        return res[:-1]
