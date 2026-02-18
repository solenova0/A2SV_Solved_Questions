class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        P = 0
        for i in range(len(nums)-2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                P = nums[i] + nums[i + 1] + nums[i + 2]
                break
        return P