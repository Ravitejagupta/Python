class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        r = ""
        c = 0
        for i in range(0,len(s),k):
            if c%2 == 0:
                r += s[i:i+k][::-1]
            else:
                r += s[i:i+k]
            c+=1
        return r
            
