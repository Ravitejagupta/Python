class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        d = {}
        min_val = 0
        for i,v in enumerate(S):
            if v in d:
                arr = d[v]
                arr.append(i)
                d[v] = arr
            else:
                d[v] = [i]
        max_val = d[S[0]][-1]
        res = []
        for i,v in enumerate(S):
            if d[v][0] > max_val:
                res.append(max_val)
                max_val = d[v][-1]
            else:
                max_val = max(max_val, d[v][-1])
        res.append(max_val)
        ans = [res[0] + 1]
        for i in range(1,len(res)):
            ans.append(res[i] - res[i-1])
        return ans
