class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        res = []
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        d1 = {}
        for key in d:
            if d[key] in d1:
                arr = d1[d[key]]
                arr.append(key)
                d1[d[key]] = arr
            else:
                d1[d[key]] = [key]
        c = 0
        s = sorted(list(d1.keys()), reverse = True)
        while c<=k:
            for i in s:
                arr = d1[i]
                res += sorted(arr)
                c += len(d1[i])
        return res[:k]
