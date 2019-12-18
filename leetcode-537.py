class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        if a is None:
            return b
        if b is None:
            return a
        Ar, Ac = a.split('+')
        Ac = Ac[:-1]
        Br, Bc = b.split('+')
        Bc = Bc[:-1]
        ans = str(int(Ar)*int(Br) - int(Ac)*int(Bc)) + '+' + str(int(Ac)*int(Br) + int(Bc)*int(Ar)) + 'i'
        return ans
        
