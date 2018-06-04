class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0 or c == 1:
            return True
        i = 0
        while i*i < c:
            if int((c -i*i)**0.5) == (c-i*i)**0.5:
                return True
            i+=1
        return False
