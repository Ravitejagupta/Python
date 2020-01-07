class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if text2[i-1] == text1[j-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])
        return matrix[-1][-1]
