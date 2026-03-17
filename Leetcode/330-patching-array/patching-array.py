class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        upto = 1
        count = 0
        i = 0
        while upto <= n:
            if i < len(nums) and nums[i] <= upto:
                upto += nums[i]
                i += 1
            else:
                upto += upto
                count  += 1

        return count
