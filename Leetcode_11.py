class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        l=0
        r =len(height)-1
        while(l<r): 
        # for x in range(len(height)):
            # for y in range(x,len(height)):
            maxarea = max(maxarea,(r-l)*min(height[l],height[r]))
            if (height[l] < height[r]):
                l+=1
            else:
                r=r-1
        return maxarea
