class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        if len(s1) == 1:
            return (s1 in s2)
        d1 = {}
        d2 = {}
        k = len(s1)
        for ch in s1:
            if ch in d1:
                d1[ch] += 1
            else:
                d1[ch] = 1
        for ch in s2[:k]:
            if ch in d2:
                d2[ch] += 1
            else:
                d2[ch] = 1
        if d1 == d2:
            return True
        for index,val in enumerate(s2[1:-k+1]):
            if d2[s2[index]] == 1:
                del d2[s2[index]]
            else:
                d2[s2[index]] -=1
            
            if s2[index+k] in d2:
                d2[s2[index+k]] +=1
            else:
                d2[s2[index+k]] = 1
            if d1 == d2:
                return True
        return False
            
