class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        mod = grid[0][0] % x
        
        for row in grid:
            for val in row:
                if val % x != mod:
                    return -1
                nums.append(val)
        
        nums.sort()
        median = nums[len(nums) // 2]
        
        op = 0
        for val in nums:
            op += abs(val - median) // x
        
        return op