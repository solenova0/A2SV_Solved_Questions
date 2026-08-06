class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def rotates(l , r):
            while l <= r:
                nums[r] , nums[l] = nums[l] , nums[r]
                l += 1
                r -= 1

        rotates(0 , n - 1)
        rotates(0 , k - 1)
        rotates( k , n- 1)