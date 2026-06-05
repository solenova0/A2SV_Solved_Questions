class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hold = -prices[0]
        # sold = 0
        # rest = 0

        # for price in prices[1:]:
        #     prev_hold = hold
        #     prev_sold = sold
        #     prev_rest = rest

        #     hold = max(prev_hold, prev_rest - price)
        #     sold = prev_hold + price
        #     rest = max(prev_rest, prev_sold)

        # return max(sold, rest)
        n = len(prices)

        @cache
        def dfs(i, holding):
            if i >= n:
                return 0

            ans = dfs(i + 1, holding)

            if holding:
                ans = max(
                    ans,
                    prices[i] + dfs(i + 2, 0) 
                )
            else:
                ans = max(
                    ans,
                    -prices[i] + dfs(i + 1, 1)
                )

            return ans

        return dfs(0, 0)