class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r_max = [max(i) for i in grid]
        c_max = []
        for i in range(len(grid)):
            m = -1
            for j in grid:
                m = max(m,j[i])
            c_max.append(m)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(r_max[i],c_max[j]) - grid[i][j]
        return ans
