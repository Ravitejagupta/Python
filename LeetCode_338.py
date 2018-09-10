def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r = [0]*(num+1)
        l = 1
        diff = 1
        for i in range(1,num+1):
            if l == i:
                l = l*2
                r[i] = 1
            elif i<l:
                r[i] = r[i-int(l/2)] + 1
        return(r)
