class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')

        dp = [INF] * (amount + 1)
        dp[0] = 0

        for target in range(1, amount + 1):
            for coin in coins:
                if target >= coin:
                    dp[target] = min(
                        dp[target],
                        dp[target - coin] + 1
                    )
        return dp[amount] if dp[amount] != INF else -1



    #Bottom-up solution