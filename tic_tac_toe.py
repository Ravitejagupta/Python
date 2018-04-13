class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        ans = 'True'
        tx = ty = 0
        x = 0
        o = 0
        cx = co = 0
        s = [ [[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]], [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[2,0],[2,1],[2,2]],                 [[0,0],[1,1],[2,2]], [[0,2],[1,1],[2,0]] ]
        X = []
        Y = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    x +=1
                    X.append([i,j])
                elif board[i][j] == 'O':
                    o +=1
                    Y.append([i,j])
        if o > x or x-o >1:
            return False
        for i in s:
            for j in i:
                if j in X:
                    cx += 1
                if j in Y:
                    co += 1
            if cx == 3 or co == 3:
                if cx == 3:
                    tx += 1
                if co == 3:
                    ty += 1
                if x-o ==0 or x-o == 1:
                    ans = True
                else:
                    ans = False
            cx = co = 0
        if tx != 0 and ty != 0: 
            return False
        elif tx == 0 and ty == 0:
            return True
        else:
            if tx != 0:
                if x - o == 1:
                    return True
                else:
                    return False
            else:
                if x - o == 0:
                    return True
                else:
                    return False
            
