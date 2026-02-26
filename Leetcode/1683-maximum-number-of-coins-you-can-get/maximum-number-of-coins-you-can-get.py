class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        left = 0
        right = n-2
        coins = 0
        while left < right:
            coins += piles[right]
            right -= 2
            left += 1 
        return coins