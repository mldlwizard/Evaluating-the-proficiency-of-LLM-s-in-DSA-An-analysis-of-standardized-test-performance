from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        n = len(prices)
        cash, hold = 0, -prices[0]

        for i in range(1, n):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])

        return cash