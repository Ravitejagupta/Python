class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        counter = 0
        if len(stones) <=1:
            return True
        if len(stones) == 2:
            return (stones[1] == 1)
        a = set()
        for i in range(1,len(stones)-1):
            a.add((stones[i],stones[i] - stones[i-1]))
            if self.ans(stones[i:],stones[i] - stones[i-1], a) or self.ans(stones[i:],stones[i] - stones[i-1] +1, a ) or self.ans(stones[i:],stones[i] - stones[i-1] -1, a):
                return True
            else:
                return False
        return False
    
    def ans(self,stones, step, set_a):
        if len(stones) <= 1:
            return True
        for i in range(1,len(stones)):
            if stones[i] - stones[0] == step and ((stones[i],step) not in set_a):
                set_a.add((stones[i],step))
                set_a.add((stones[i],step + 1))
                set_a.add((stones[i],step - 1))
                if self.ans(stones[i:], stones[i] - stones[0], set_a) or self.ans(stones[i:], stones[i] - stones[0] + 1, set_a) or self.ans(stones[i:], stones[i] - stones[0] -1, set_a):
                    return True
        
            
        
