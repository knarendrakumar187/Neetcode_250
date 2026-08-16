class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # recurrence:
        # on day i what is the max profit you can make
        # let j < i
        # max(i) = max(j) + max(buying on day j and selling on day i)
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit