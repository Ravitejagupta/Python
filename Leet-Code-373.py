import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        total = len(nums1)*len(nums2)
        r = []
        for i in nums1:
            for j in nums2:
                r.append([i+j,i,j])
        heapq.heapify(r)
        res = []
        for _ in range(k):
            if total > 0:
                popped = heapq.heappop(r)
                res.append(popped[1:])
                total -=1
            else:
                return res
        return res
