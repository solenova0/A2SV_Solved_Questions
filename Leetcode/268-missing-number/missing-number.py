class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n - 1  == nums[n - 1]:
            return n
        for i in range(n):
            if i == nums[i]:
                continue
            else:
                return i
        