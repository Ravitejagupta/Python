class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        ans = 0
        target = abs(target)
        if target == 1:
            return 1
        c = 0
        s = 0
        while True:
            if s >= target:
                break
            c+=1
            s +=c
        print(s,c)
        if s == target:
            return c
        if (s + c + 1 - target)%2 == 0:
            ans = c+1
        if (s - target)%2 == 0:
            return c
        else:
            s_minus = s - c
            if ans != 0:
                return min((c-1 + 2*(target-s_minus)), c+2, ans)
            else:
                return min((c-1 + 2*(target-s_minus)), c+2 )
                
