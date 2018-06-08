class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target is None or not matrix:
            return False
        
        r,c = len(matrix),len(matrix[0]) 
        low, high = 0, r*c- 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid//c][mid % c]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
