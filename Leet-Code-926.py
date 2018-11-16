class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        ones = 0
        for i in S:
            if i == '1':
                ones += 1
        ans = 100000
        temp = 0
        l = len(S)
        for i in range(len(S)):
            if S[i] == '0':
                ans  = min(ans, temp + l - ones - i -1)
            else:
                ones -= 1
                ans = min(ans, temp + l - ones -i - 1)
                temp += 1
        return ans
