class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            n = len(matrix)

            for r in range(n):
                for c in range(r + 1, n):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

            for row in matrix:
                row.reverse()

        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)

        return False
