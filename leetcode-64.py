#Time complexity is mn*log(O(mn)) can be in O(mn) using dp

import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = set((0,0))
        l = [(grid[0][0],(0,0))]
        heapq.heapify(l)
        directions = [(0,1),(1,0)]
        while l:
            p = heapq.heappop(l)
            if p[1] == (len(grid)-1, len(grid[0])-1):
                return p[0]
            x,y = p[1]
            for dx,dy in directions:
                if x+dx in range(0,len(grid)) and y+dy in range(0,len(grid[0]))  and (x+dx,y+dy) not in visited:
                    heapq.heappush(l, (p[0]+ grid[x+dx][y+dy], (x+dx,y+dy)))
                    visited.add((x+dx,y+dy))
        
