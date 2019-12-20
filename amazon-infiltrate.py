import copy

grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def infiltrate(grid):
    visited = set()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    c = 0
    ans = 0
    while c < len(grid)**2:
        temp = copy.deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid)):
                for d in directions:
                    if (i+d[0]) in range(len(grid)) and (j+d[1]) in range(len(grid)) and (i+d[0],j+d[1]) not in visited and grid[i][j] == 1:
                        visited.add((i+d[0], j+d[1]))
                        if not (i,j) in visited:
                            visited.add((i,j))
                            c += 1
                        c += 1
                        temp[i+d[0]][j+d[1]] = 1
        grid = copy.deepcopy(temp)
        ans += 1
        if grid == temp:
            return -1
    return ans

print("ans is " + str(infiltrate(grid)))
