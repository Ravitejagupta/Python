class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            m = min(S)
            parts = S.split(m)
            parts[-1] += parts[0]
            parts = parts[1:]
            index = parts.index(min(parts))
            parts =  parts[index:] + parts[:index]
            res = ""
            for p in parts:
                res += m+p
            return res  
        return ''.join(sorted(S))
