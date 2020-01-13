ans = []

def queens(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    ans  = []
    def helper(n, res):
        if n == len(matrix):
            return res
        for i in range(len(matrix)):
            status = True
            if matrix[n][i] == 0:
                for j in range(len(matrix)):
                    if matrix[j][i] == 1:
                        status = False
                        break
                if status:
                    for j in range(len(matrix)):
                        if (i-j) in range(len(matrix)) and (n-j) in range(len(matrix)) and matrix[n-j][i-j] == 1 or (i+j) in range(len(matrix)) and (n-j) in range(len(matrix)) and matrix[n-j][i+j] == 1:
                            status = False
                            break
                if status:
                    matrix[n][i] = 1
                    temp = helper(n+1, res+str(i+1))
                    if temp:
                        ans.append(temp)
                    matrix[n][i] = 0  
                        
    helper(0,"")
    return ans

print(queens(4))                        
