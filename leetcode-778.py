import heapq
grid = [[0,2],[1,3]]
def swimInWater(grid):    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = set()
    visited.add((0,0))
    l = [[grid[0][0],0,0]]
    heapq.heapify(l)
    while True:
        popped = heapq.heappop(l)
        if popped[1:] == [len(grid)-1, len(grid)-1]:
            return popped[0]
        for d in directions:
            if (popped[1]+d[0]) in range(len(grid)) and (popped[2]+d[1]) in range(len(grid)) and (popped[1]+d[0],popped[2]+d[1]) not in visited:
                heapq.heappush(l, [max(popped[0], grid[popped[1]+d[0]][popped[2]+d[1]]), popped[1]+d[0], popped[2]+d[1]])
                visited.add((popped[1]+d[0], popped[2]+d[1]))

print(swimInWater(grid))
