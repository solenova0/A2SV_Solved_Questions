class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        low , mid = 0, 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 2:
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high -= 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[low] , nums[mid] = nums[mid] , nums[low]
                mid += 1
                low += 1