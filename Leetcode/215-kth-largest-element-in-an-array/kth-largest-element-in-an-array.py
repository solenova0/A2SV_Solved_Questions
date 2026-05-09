class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = nlargest(k , nums)
        return res[-1]