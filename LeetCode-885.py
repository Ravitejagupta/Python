class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        up = False
        right = True
        c = 1
        step = 1
        result = [[r0,c0]]
        while c < R*C:
            if not up:
                for _ in range(step):
                    c0 +=1
                    if c0 in range(0,C) and r0 in range(0,R):
                        result.append([r0,c0])
                        c+=1
                for _ in range(step):
                    r0 += 1
                    if c0 in range(0,C) and r0 in range(0,R):
                        result.append([r0,c0])
                        c+=1
                up = True
                step += 1
            else:
                for _ in range(step):
                    c0 -=1
                    if c0 in range(0,C) and r0 in range(0,R):
                        result.append([r0,c0])
                        c+=1
                for _ in range(step):
                    r0 -= 1
                    if c0 in range(0,C) and r0 in range(0,R):
                        result.append([r0,c0])
                        c+=1
                up = False
                step +=1
        return result
