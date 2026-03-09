class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
    
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        total_water = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    total_water += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    total_water += r_max - height[r]
                r -= 1
                
        return total_water