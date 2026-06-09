class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        min_ = nums[0] 
        max_ = nums[0]

        for v in nums:
            min_ = min(min_, v)
            max_ = max(max_, v)

        ans = (max_ - min_) * k

        return ans