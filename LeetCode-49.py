class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        r = []
        index = 0
        for i in strs:
            s = ''.join(sorted(i))
            if s in d:
                r[d[s]].append(i)
            else:
                d[s] = index
                r.append([])
                r[index].append(i)
                index +=1
        return r
