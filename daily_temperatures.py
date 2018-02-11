class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l = len(temperatures)
        ans = [0]*l
        ans[l-1] = 0
        m = temperatures[l-1]
        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i] < temperatures[i+1]:
                ans[i] = 1
            elif temperatures[i] >= m:
                ans[i] = 0
                #if temperatures[i] > m:
                m = temperatures[i]
            else:
                for j in range(i+1,l):
                    if temperatures[i] < temperatures[j]:
                        ans[i] = j-i
                        break
        return ans
