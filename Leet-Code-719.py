import heapq
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count  = 0
        ans = 0
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        keys = list(d.keys())
        res = []
        for i in range(len(keys)):
            for j in range(i,len(keys)):
                if i == j and d[keys[i]] ==1:
                    pass
                else:
                    res.append([abs(keys[i] - keys[j]), keys[i], keys[j]])
        heapq.heapify(res)
        while True:
            if count >= k:
                return ans
            popped = heapq.heappop(res)
            if popped[1] == popped[2]:
                count += int(d[popped[1]]*(d[popped[1]] -1) / 2)
            else:
                count += d[popped[1]]*d[popped[2]]
            ans = abs(popped[1] - popped[2])
        return abs(popped[1] - popped[2])
                    
