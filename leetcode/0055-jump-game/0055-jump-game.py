class Solution:
    def canJump(self, nums: List[int]) -> bool:
        v = 0
        for i,n in enumerate(nums):
            if i > v:
                return False
            v = max(v, i+n)
        return True
       