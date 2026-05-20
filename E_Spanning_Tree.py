# import sys
# input = sys.stdin.readline

# class DSU:
#     def __init__(self, n):
#         self.parent = list(range(n + 2))
#         self.size = [1] * (n + 2)

#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, a, b):
#         a = self.find(a)
#         b = self.find(b)

#         if a == b:
#             return

#         if self.size[a] < self.size[b]:
#             a, b = b, a

#         self.parent[b] = a
#         self.size[a] += self.size[b]


# n, q = map(int, input().split())

# dsu = DSU(n)

# # next unprocessed position
# nxt = list(range(n + 2))


# def get_next(x):
#     if nxt[x] != x:
#         nxt[x] = get_next(nxt[x])
#     return nxt[x]


# for _ in range(q):
#     t, x, y = map(int, input().split())

#     if t == 1:
#         dsu.union(x, y)

#     elif t == 2:
#         cur = get_next(x)

#         while cur < y:
#             dsu.union(cur, cur + 1)

#             # remove cur from future processing
#             nxt[cur] = get_next(cur + 1)

#             cur = get_next(cur)

#     else:
#         if dsu.find(x) == dsu.find(y):
#             print("YES")
#         else:
#             print("NO")


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


n, m = map(int, input().split())

edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()
dsu = DSU(n)

mst_weight = 0

for w, u, v in edges:
    if dsu.union(u, v):
        mst_weight += w

print(mst_weight)