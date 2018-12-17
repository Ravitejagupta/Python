class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = arr[0]
        dummy = [m]
        for i in arr[1:]:
            if i >=m:
                m = max(i,m)
                dummy.append(m)
            else:
                for j,val in enumerate(dummy):
                    if i < val:
                        if j == 0:
                            dummy = [max(dummy)]
                            break
                        else:
                            dummy = dummy[:j] + [max(dummy)]
                            break
        return len(dummy)
                        
