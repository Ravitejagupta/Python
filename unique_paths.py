class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n ==1 :
            return 1
        return int((math.factorial(m+n-2)/math.factorial(m-1))/math.factorial(n-1))
