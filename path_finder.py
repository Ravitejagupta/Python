M = [[0,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1,]]

def pathFinder(M, position, N):
    if M[0][0] == 0:
        return None
    if position == [N-1,N-1]:
        return []
    x,y = position
    if x+1 < N and M[x+1][y] == 1:
        p = pathFinder(M,[x+1,y],N)
        if p is not None:
            return [(x+1,y)] + p
    if y+1 < N and M[x][y+1] == 1:
        q = pathFinder(M,[x,y+1],N)
        if q is not None:
            return [(x,y+1)] + q

print(pathFinder(M,[0,0], 4))
    
