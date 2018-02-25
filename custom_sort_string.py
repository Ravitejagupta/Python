class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        ans = ''
        for i in S:
            if T.count(i) != 0:
                ans += i*T.count(i)
        for j in T:
            if j not in ans:
                ans+= j*T.count(j)
        return ans
