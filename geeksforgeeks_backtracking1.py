arr1 = [[1, 0, 0, 0],
       [1, 1, 0, 1], 
       [0, 1, 0, 0], 
       [0, 1, 1, 1]]

arr =  [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]

def findPath(arr, n):
    # code here
    ans  = []
    d = {'R':(0,1),'L':(0,-1),'D':(1,0),'U':(-1,0)}
    def helper(matrix, res, cur, visited):
        visited.add(cur)
        if cur == (n-1,n-1):
            return res
        if matrix[cur[0]][cur[1]] == 1:
            for k in list(d.keys()):
                if cur[0] + d[k][0] in range(n) and cur[1] + d[k][1] in range(n) and matrix[cur[0] + d[k][0]][cur[1] + d[k][1]] == 1 and (cur[0] + d[k][0], cur[1] + d[k][1]) not in visited:
                    temp = helper(matrix, res + k, (cur[0] + d[k][0], cur[1] + d[k][1]), visited)
                    if temp: ans.append(temp)
                    visited.remove((cur[0] + d[k][0], cur[1] + d[k][1]))
            return None
    helper(arr, "", (0,0), set())
    return ans

print(findPath(arr, 4))
