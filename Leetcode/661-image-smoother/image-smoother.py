class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        
        direc = [ (-1, -1), (-1, 0), (-1, 1),(0, -1),  (0, 0),  (0, 1),(1, -1),  (1, 0),  (1, 1)
        ]
        
        res = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                total = 0
                count = 0
                
                for dr, dc in direc:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols:
                        total += img[nr][nc]
                        count += 1
                
                res[r][c] = total // count
        
        return res