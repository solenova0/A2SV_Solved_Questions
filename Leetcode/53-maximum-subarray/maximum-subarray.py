class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum , curr_sum)

            if curr_sum < 0:
                curr_sum = 0
        return max_sum
        # max_sum = current_sum = nums[0]
        # start = end = temp_start = 0
        
        # for i in range(1, len(nums)):
        #     if nums[i] > current_sum + nums[i]:
        #         current_sum = nums[i]
        #         temp_start = i
        #     else:
        #         current_sum += nums[i]
            
        #     if current_sum > max_sum:
        #         max_sum = current_sum
        #         start = temp_start
        #         end = i
        
        # return max_sum
