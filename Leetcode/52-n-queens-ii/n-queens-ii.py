class Solution:
    def totalNQueens(self, n: int) -> int:
        clmn = set()
        rightD = set()
        leftD = set() 
        
        ans = []
        temp = [["."] * n for _ in range(n)]

        def solve(r):
            if r == n:
                copy = ["".join(row) for row in temp]
                ans.append(copy)
                return

            for c in range(n):
                if c in clmn or (r + c) in rightD or (r - c) in leftD:
                    continue
             
                clmn.add(c)   #queens
                rightD.add(r + c)
                leftD.add(r - c)
                temp[r][c] = "Q"

                solve(r + 1)

                clmn.remove(c)  # Back-track
                rightD.remove(r + c)
                leftD.remove(r - c)
                temp[r][c] = "."
        solve(0)
        return len(ans)