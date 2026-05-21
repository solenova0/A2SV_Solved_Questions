class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.myfun(nums[1:]), self.myfun(nums[:-1]))

    def myfun(self, nums):
        a, b = 0, 0

        for n in nums:
            temp = max(a + n, b)
            a = b
            b = temp
        return b



