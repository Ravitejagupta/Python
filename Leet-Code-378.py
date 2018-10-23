import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ##Sorting ##
        '''r = []
        for i in matrix:
            r += i
        r = sorted(r)
        return r[k-1]'''
        ## Constructinf a heap ##
        r = []
        for row in matrix:
            r += row
        heapq.heapify(r)
        for _ in range(k-1):
            heapq.heappop(r)
        return heapq.heappop(r)
