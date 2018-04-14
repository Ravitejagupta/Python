class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        price = 100000
        for i in prices:
            price = min(price, i)
            ans = max(ans, i-price)
        return ans
            
                
