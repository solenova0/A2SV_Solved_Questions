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

    rev = [[] for _ in range(n + 1)]
    outdeg = [0] * (n + 1)

    for _ in range(m):
        u, v = mapinput()
        rev[v].append(u)
        outdeg[u] += 1

    pq = []

    for i in range(1, n + 1):
        if outdeg[i] == 0:
            heapq.heappush(pq, -i)

    label = [0] * (n + 1)

    cur = n

    while pq:
        u = -heapq.heappop(pq)

        label[u] = cur
        cur -= 1

        for p in rev[u]:
            outdeg[p] -= 1

            if outdeg[p] == 0:
                heapq.heappush(pq, -p)

    print(*label[1:])

for _ in range(test_cases(1)):
    solve()


