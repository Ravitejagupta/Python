class Solution(object):
    def build_heap(self,arr):
        res = [arr[0]]
        for i in range(1,len(arr)):
            index = i
            res.append(arr[i])
            while index >=0 and ((index+1)//2) -1 >=0:
                if res[((index+1)//2) -1] > res[index]:
                    res[((index+1)//2) -1], res[index] = res[index], res[((index+1)//2) -1]
                    index = ((index+1)//2) -1

                else:
                    break
        return res

    def pop(self,arr):
        ans = arr[0]
        index = 0
        while index < len(arr):
            if index*2 +2 < len(arr) and arr[index*2 + 1] is not None and arr[index*2 +2] is not None :
                if arr[index*2 + 1] < arr[index*2 +2]:
                    arr[index] = arr[index*2 + 1]
                    arr[index*2 + 1] = None
                    index = index*2 + 1
                else:
                    arr[index] = arr[index*2 + 2]
                    arr[index*2 + 2] = None
                    index = index*2 + 2
            elif index*2 + 1 < len(arr) and arr[index*2 + 1] is not None:
                arr[index] = arr[index*2 + 1]
                arr[index*2 + 1] = None
                index = index*2 + 1
            elif index*2 + 2 < len(arr) and arr[index*2 + 2] is not None:
                arr[index] = arr[index*2 + 2]
                arr[index*2 + 2] = None
                index = index*2 + 2
            else:
                break
        arr = arr[1:]
        return ans
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        r = [-1*num for num in nums]
        r = self.build_heap(r)
        for _ in range(k-1):
            self.pop(r)
        return self.pop(r) * -1        
