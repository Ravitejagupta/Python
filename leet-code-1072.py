class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = {}
        def inverse(r):
            res = ""
            for i in r:
                if i == '0':
                    res += '1'
                else:
                    res += '0'
            return res
        
        for row in matrix:
            r = ''.join([str(i) for i in row])
            if r in d:
                d[r] += 1
            else:
                ri = inverse(r)
                if ri in d:
                    d[ri] += 1
                else:
                    d[r] = 1
        return max(d.values())
                
