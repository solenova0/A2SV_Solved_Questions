from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        queue = deque()
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    queue.append((r, c))

        for c in range(cols):
            for r in [0, rows - 1]:
                if board[r][c] == 'O':
                    queue.append((r, c))

        dir = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()

            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'T'  

                for dr, dc in dir:
                    queue.append((r + dr, c + dc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X' 
                elif board[r][c] == 'T':
                    board[r][c] = 'O'  