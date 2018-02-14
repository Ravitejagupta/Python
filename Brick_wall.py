class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        m = 0
        d={}
        for i in wall:
            dummy = 0
            for j in i[:-1]:
                dummy +=j
                if dummy in d:
                    d[dummy] +=1
                    m = max(m,d[dummy])
                else:
                    d[dummy] = 1
                    m = max(1,m)
        return len(wall) - m
