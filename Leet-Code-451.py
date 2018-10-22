class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        res = ""
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        d1 = {}
        for key in d:
            if d[key] in d1:
                arr = d1[d[key]]
                arr.append(key)
                d1[d[key]] = arr
            else:
                d1[d[key]] = [key]
        arr = sorted(list(d1.keys()), reverse = True)
        for val in arr:
            a = [i*val for i in d1[val]]
            res += ''.join(a)
        return res
