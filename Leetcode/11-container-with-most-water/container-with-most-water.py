class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        maxx = 0
        while l <= r:
            w = r - l
            if height[l] > height[r]:
                v = w * height[r]
                r -= 1
            else:
                v = w * height[l]
                l += 1
            maxx = max(maxx , v)
        return maxx


        