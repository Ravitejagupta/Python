class Solution:
    def numDecodings(self, s):
        ans1 = 1
        ans2 = 1
        if len(s) <=1:
            try:
                if int(s) not in range(1,26):
                    return 0
                else:
                    return 1
            except:
                return 0
        else:
            if s.startswith('0') or s.find('00') !=-1:
                return 0
            for i in range(1,len(s)):
                if s[i] == '0':
                    ans1 = 0
                if (s[i-1] == '1' or s[i-1] == '2' and int(s[i]) <=6):
                    ans1 = ans2 + ans1
                    ans2 = ans1 - ans2
                else:
                    ans2 = ans1
        return ans1
