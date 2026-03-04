class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        summ = 0
        total = 0
        for v in nums:
            summ += v
            total = min(total , summ)
        if total > 0:
            return 1
        else:
            return abs(total) + 1