class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split()
        asn = ""
        for i in a:
            asn += i[::-1] + " "
        return asn[:-1]
