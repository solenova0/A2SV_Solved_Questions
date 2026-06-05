
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.size[a] < self.size[b]:
            a, b = b, a

        self.parent[b] = a
        self.size[a] += self.size[b]

        return True


n, m1, m2 = map(int, input().split())

dsu1 = DSU(n)
dsu2 = DSU(n)

for _ in range(m1):
    u, v = map(int, input().split())
    dsu1.union(u, v)

for _ in range(m2):
    u, v = map(int, input().split())
    dsu2.union(u, v)

ans = []

for u in range(1, n + 1):
    for v in range(u + 1, n + 1):

        if dsu1.find(u) != dsu1.find(v) and \
           dsu2.find(u) != dsu2.find(v):

            dsu1.union(u, v)
            dsu2.union(u, v)

            ans.append((u, v))

print(len(ans))

for u, v in ans:
    print(u, v)