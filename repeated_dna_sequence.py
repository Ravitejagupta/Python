class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        r = []
        for i in range(len(s)-10+1):
            seq = s[i:i+10]
            if seq in d:
                if d[seq] == 1:
                    r.append(seq)
                d[seq] +=1
            else:
                d[seq] = 1
        return r
