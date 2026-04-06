class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        drcn = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        x = y = 0
        set1 = set(map(tuple, obstacles))
        
        maxx = 0
        
        for cmd in commands:
            if cmd == -1:  
                d = (d + 1) % 4
            elif cmd == -2:  
                d = (d - 1) % 4
            else:
                dx, dy = drcn[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in set1:
                        break
                    x, y = nx, ny
                    maxx = max(maxx, x*x + y*y)
        
        return maxx