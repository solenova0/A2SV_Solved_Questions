class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        length = 0
        l = 0
        i = l
        while i < n:
            if nums[l] *k >= nums[i]:
                i += 1
            else:
                l += 1
            length = max(length, i-l)
        return n-length



        
        