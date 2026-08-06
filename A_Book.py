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

    g = [[] for _ in range(n)]
    indeg = [0] * n

    for i in range(n):
        arr = listinput()

        k = arr[0]

        for x in arr[1:]:
            x -= 1

            g[x].append(i)
            indeg[i] += 1

    q = deque()
    dp = [1] * n

    for i in range(n):
        if indeg[i] == 0:
            q.append(i)

    cnt = 0

    while q:
        u = q.popleft()
        cnt += 1

        for v in g[u]:

            if u < v:
                dp[v] = max(dp[v], dp[u])
            else:
                dp[v] = max(dp[v], dp[u] + 1)

            indeg[v] -= 1

            if indeg[v] == 0:
                q.append(v)

    if cnt != n:
        print(-1)
    else:
        print(max(dp))

for _ in range(test_cases()):
    solve()


