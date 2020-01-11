from collections import deque

grid1 = [['R', 'L', 'R', 'L', 'R'],
        ['L', 'U', 'R', 'R', 'R'],
        ['R', 'D', 'R', 'R', 'D'],
        ['R', 'L', 'L', 'L', 'L'],
        ['L', 'R', 'U', 'U', 'R']]

grid = [['R', 'R', 'R', 'R', 'D'],
        ['L', 'U', 'R', 'R', 'D'],
        ['R', 'D', 'R', 'R', 'D'],
        ['R', 'L', 'L', 'L', 'D'],
        ['L', 'R', 'U', 'U', 'R']]

def min_modifications(grid):
    if len(grid) <= 1:
        retuurn 0
    d = {'L':[0,-1], 'R':[0,1], 'U':[-1,0], 'D':[1,0]}
    visited = set()
    matrix = [[1000 for _ in grid] for _ in grid[0]]
    matrix[0][0] = 0

    q = deque()
    q.append((0,0))
    while q:
        cur = q.popleft()
        visited.add(cur)
        for direction in list(d.values()):
            if cur[0] + direction[0] in range(len(grid)) and cur[1] + direction[1] in range(len(grid[0])) and (cur[0]+direction[0],cur[1]+direction[1]) not in visited:
                q.append((cur[0] + direction[0], cur[1] + direction[1]))
                #if grid[cur[0] + direction[0]][cur[1] + direction[1]] == d[:
                if direction == d[grid[cur[0]][cur[1]]]:
                    matrix[cur[0] + direction[0]][cur[1] + direction[1]] = min(matrix[cur[0] + direction[0]][cur[1] + direction[1]], matrix[cur[0]][cur[1]])
                else:
                    matrix[cur[0] + direction[0]][cur[1] + direction[1]] = min(matrix[cur[0] + direction[0]][cur[1] + direction[1]], matrix[cur[0]][cur[1]]+ 1)
    return matrix[-1][-1]

print(min_modifications(grid))
print(min_modifications(grid1))
