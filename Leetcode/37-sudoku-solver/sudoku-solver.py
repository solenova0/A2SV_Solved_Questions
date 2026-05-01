class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3)*3 + j//3].add(num)

        def backtrack():
            if not empty:
                return True

            min_options = 10
            idx = -1

            for k in range(len(empty)):
                i, j = empty[k]
                options = 0
                for num in "123456789":
                    if num not in rows[i] and num not in cols[j] and num not in boxes[(i//3)*3 + j//3]:
                        options += 1
                
                if options < min_options:
                    min_options = options
                    idx = k

            i, j = empty.pop(idx)
            box_id = (i//3)*3 + j//3

            for num in "123456789":
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:
                    
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_id].add(num)

                    if backtrack():
                        return True
                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_id].remove(num)

            empty.insert(idx, (i, j))
            return False

        backtrack()