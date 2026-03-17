class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = list(range(1, n+1))
        idx = 0
        while len(res) > 1:
            idx = (idx + k - 1) % len(res)
            res.pop(idx)
        return res[0]  