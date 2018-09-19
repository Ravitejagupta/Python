class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key = lambda x: -1 * len(x))
        words_set = set(words)
        ans = 0
        for i in words:
            if i in words_set:
                ans += len(i) + 1
                for j in range(len(i)):
                    if i[j:] in words_set:
                        words_set.remove(i[j:])
        return ans
