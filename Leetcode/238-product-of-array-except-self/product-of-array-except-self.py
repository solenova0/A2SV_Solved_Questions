class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        v = 1
        for i in reversed(range(n)):
            res[i] *= v
            v *= nums[i]

        return res