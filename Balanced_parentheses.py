class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {']':'[','}':'{',')':'('}
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if stack == []:
                    return False
                if d[i] != stack.pop():
                    return False
            else:
                return False
        return (len(stack) == 0)
