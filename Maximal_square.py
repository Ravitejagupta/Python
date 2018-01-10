class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        result = [[int(i) for i in j] for j in matrix]
        ans = 0
        for x in range(len(result)):
            for y in range(len(result[0])):
                if x == 0:
                    if result[x][y] == 1:
                        ans+=1
                        break
                if result[x][y] == 1 and y !=0:
                    result[x][y] = min(result[x-1][y], result[x-1][y-1], result[x][y-1]) + 1
                    if result[x][y] > ans:
                        ans = result[x][y]
        if ans == 0:
            for i in range(len(matrix)):
                if matrix[i][0] == '1':
                    return 1
        return ans*ans
                    
                                
        
