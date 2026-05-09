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
    input()  
    n, k = mapinput()
    g = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)

    for _ in range(n - 1):
        u, v = mapinput()
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    q = deque()
    dist = [0] * (n + 1)

    for i in range(1, n + 1):
        if deg[i] <= 1:
            q.append(i)
            dist[i] = 1

    while q:
        u = q.popleft()

        for v in g[u]:
            deg[v] -= 1

            if deg[v] == 1:
                dist[v] = dist[u] + 1
                q.append(v)

    ans = 0
    for i in range(1, n + 1):
        if dist[i] > k:
            ans += 1

    print(ans)
    
for _ in range(test_cases()):
    solve()