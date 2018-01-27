class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        a = [1]*len(s)
        for i in range(1,len(s)):
            if s[i] not in s[i-a[i-1]:i]:
                #print(s[i-a[i-1]:i])
                a[i] = a[i-1] + 1
            else:
                a[i] = i - s[:i].rfind(s[i])
        print(a)
        return(max(a))
