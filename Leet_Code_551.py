class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'LLL' in s or s.count('A') > 1:
            return False
        return True
