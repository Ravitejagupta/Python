class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for i in arr1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = []
        for i in arr2:
            ans += [i]*d[i]
            d.pop(i)
        for key in sorted(list(d.keys())):
            ans += [key]*d[key]
        return ans
