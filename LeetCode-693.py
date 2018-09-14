class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n%2
        n = int(n/2)
        while n > 0:
            if a == n%2:
                return False
            a = n%2
            n = int(n/2)
        return True
