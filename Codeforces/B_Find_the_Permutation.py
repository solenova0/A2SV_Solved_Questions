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
    n = num()
    g = [word() for _ in range(n)]

    adj = [[] for _ in range(n)]
    indeg = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if g[i][j] == '1':
                adj[i].append(j)
                indeg[j] += 1

    q = deque()

    for i in range(n):
        if indeg[i] == 0:
            q.append(i)

    res = []
    while q:
        u = q.popleft()
        res.append(u + 1)

        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    print(*res)

for _ in range(test_cases()):
    solve()