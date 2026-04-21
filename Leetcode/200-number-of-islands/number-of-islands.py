class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        islands = 0
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(row, col):
            if row < 0 or row >= r or col < 0 or col >= c or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            for dr, dc in dir:
                i, j = row + dr, col + dc
                dfs(i, j)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        
        return islands