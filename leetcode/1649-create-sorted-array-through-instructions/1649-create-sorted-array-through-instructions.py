#Fenwick Tree Algorthim
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)
    def update(self, i):
        while i <= self.n:
            self.tree[i] += 1
            i += i & -i
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        bit = BIT(max(instructions))

        res = 0
        for i, x in enumerate(instructions):
            left = bit.query(x - 1)
            right = i - bit.query(x)
            res += min(left, right)
            bit.update(x)

        return res % MOD