class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        e1 = -1
        for i in range(len(A)-1, -1, -1):
            if A[i-1]>A[i]:
                e1 = i-1
                break
        if e1 == -1:
            return A
        val = len(A) -1
        while val > e1:
            if A[val] < A[e1] and A[val] != A[val -1]:
                A[val],A[e1] = A[e1],A[val]
                return A
            val -= 1
