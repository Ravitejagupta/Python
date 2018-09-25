class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for index, val in enumerate(t):
            if val in d:
                arr = d[val]
                arr.append(index)
                d[val] = arr
            else:
                d[val] = [index]
        val = 0
        for char in s:
            if char not in d or len(d[char]) == 0:
                return False
            else:
                if val > d[char][-1]:
                    return False
                for i,v in enumerate(d[char]):
                    if v >= val:
                        val = v
                        arr = d[char]
                        arr = arr[i+1:]
                        d[char] = arr
                        break
        return True
