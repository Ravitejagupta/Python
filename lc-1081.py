class Solution:
    def smallestSubsequence(text):
        ans = ""
        d = {}
        for i,v in enumerate(text):
            d[v] = i
        s = set()

        for i,v in enumerate(text):
            if v not in s:
                s.add(v)
                ans += v
            while len(ans) > 1:
                if ans[-2] > ans[-1] and d[ans[-2]] > i:
                    temp = ans[-2]
                    ans = ans.replace(temp, "")
                    s.remove(temp)
                else:
                    break                
        return ans
        
