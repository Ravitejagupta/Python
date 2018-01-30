class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        t = len(B)//len(A) + 2
        c = 1
        a=A
        while c!=t + 1:
            if B in A:
                return c
            else:
                A = A + a
            c = c+1
        return -1
