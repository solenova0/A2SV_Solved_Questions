class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        Min = Max = nums[0]

        for v in nums:
            Min = min(Min, v)
            Max = max(Max, v)

        return (Max - Min) * k