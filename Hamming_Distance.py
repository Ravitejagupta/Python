class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = 0
        while(x != 0 or y!=0):
            if x%2 != y%2:
                r+=1
            x = int(x/2)
            y = int(y/2)
        remainder = max(x,y)
        while(remainder !=0):
            if remainder %2 ==1:
                r+=1
                remainder = remainder/2
        return r
            
