class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
            n = len(nums) 
            opp = 0  
            prev = nums[n - 1]  

            for i in range(n - 2, -1, -1):
                if nums[i] > prev:
                    k = (nums[i] + prev - 1) // prev
                    opp += k - 1
                    prev = nums[i] // k
                else:
                    prev = nums[i]
            return opp