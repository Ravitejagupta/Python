class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        while s:
            d = {}
            for i in s:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] +=1
            first = 0
            for index,val in enumerate(s):
                if val < s[first]:
                    first = index
                d[val] -=1
                if d[val] == 0:
                    break
            r += s[first]
            s = s = s[first+1:].replace(s[first], "")
        return r
                
