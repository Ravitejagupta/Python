class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def clear(grid,r,c):
            if (r not in range(len(grid)) or c not in range(len(grid[0]))):
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            clear(grid,r-1,c)
            clear(grid,r+1,c)
            clear(grid,r,c+1)
            clear(grid,r,c-1)
        ans = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    ans +=1
                    clear(grid,row,column)
        return ans
