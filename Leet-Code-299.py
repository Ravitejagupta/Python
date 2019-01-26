class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        B = 0
        d1 = {}
        d2 = {}
        for i,v in enumerate(secret):
            if secret[i] == guess[i]:
                A += 1
            else:
                if v in d1:
                    d1[v] += 1
                else:
                    d1[v] = 1
                if guess[i] in d2:
                    d2[guess[i]] += 1
                else:
                    d2[guess[i]] = 1
        for key in d1:
            if key in d2:
                B += min(d1[key], d2[key])
        return str(A)+"A"+str(B)+"B"
