class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        l = 0
        for i in range(k):
            sum += nums[i]
        curr_max = sum
        for r in range(k , len(nums)):
            sum += nums[r] - nums[l]
            curr_max = max(curr_max, sum )
            l += 1
        return curr_max / k
    
        