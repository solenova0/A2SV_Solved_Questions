class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1 
        curr = float("inf")
        
        while l  <  r :
            mid = l + (r - l ) // 2
            curr = min(curr,nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1 
                
        return min(curr,nums[l])
        
        