def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        for i in s:
            if i in d1 :
                d1[i] +=1
            else:
                d1[i] = 1
        for i in t:
            if i in d2 :
                d2[i] += 1
            else:
                d2[i] = 1
        return (d1 == d2)
