class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        - UNDERSTAND
        input: list of int
        output: int

        idea: buy when price low and you see there's an opportunity to sell for highest
        maximize profit = sell - buy
        choose minimum value to te left of prices[i]
        if all profits are negative, return 0

        - PLAN:
        two pointer algorithm
        l - buy
        r - sell

        when prices[l] > prices[r], l = r because we know that r is a lower price
        when prices[l] < prices[r], profit = prices[r] - prices[l]
        maxProfit = max(maxProfit, profit)

        r += 1 regardless of condition b/c this is a sliding window problem

        '''
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            elif prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            r += 1
        return maxProfit