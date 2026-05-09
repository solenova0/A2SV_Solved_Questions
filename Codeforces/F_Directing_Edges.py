import sys, math, itertools, heapq
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from functools import cmp_to_key
from operator import itemgetter
from random import randint

input = sys.stdin.readline

intinput  = lambda: int(input())
strinput  = lambda: input().strip()
listinput = lambda: list(map(int, input().split()))
tupleinput= lambda: tuple(map(int, input().split()))
mapinput  = lambda: map(int, input().split())
matrixintinput = lambda n: [listinput() for _ in range(n)]
matrixstrinput = lambda n: [input().split() for _ in range(n)]

num, arr, word = intinput, listinput, strinput
words = lambda: input().split()

yn = lambda c: "YES" if c else "NO"

RANDOM = randint(1, 2**32 - 1)
xor = lambda x: x ^ RANDOM

test_cases = lambda d=0: intinput() if d == 0 else d

def solve():
    n, m = mapinput()
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    edges = []

    for _ in range(m):
        typ, u, v = mapinput()
        edges.append((typ, u, v))

        if typ == 1:
            adj[u].append(v)
            indeg[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(topo) != n:
        print("NO")
        return

    pos = [0] * (n + 1)
    for i in range(n):
        pos[topo[i]] = i

    print("YES")
    for  typ, u, v in edges:
        if typ == 1:
            print(u,v)
        else:
            if pos[u] < pos[v]:
                print(u,v)
            else:
                print(v,u)


for _ in range(test_cases()):
    solve()
    