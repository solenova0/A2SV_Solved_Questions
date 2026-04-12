class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i]
            return max(
                nums[i] - helper(i + 1, j),
                nums[j] - helper(i, j - 1)
            )
        
        return helper(0, len(nums) - 1) >= 0