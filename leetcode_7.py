class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x<-2**32 or x> 2**32):
            return 0
        if (x==0):
            return 0
        sign = x/abs(x)
        un = abs(x)
        r=0
        while(un!=0):
            r=r*10
            r=r+un%10
            un=un//10
        if (r<-2**31 or r> 2**31):
            return 0
        return r*sign
