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
    v = listinput()

    rows = []
    for _ in range(n):
        a = list(map(int, input().split()))
        a.sort(reverse=True)

        pref = [0]
        for x in a:
            pref.append(pref[-1] + x)
        rows.append(pref)

    ans = m

    dp = [-1] * (n * m + 1)
    dp[0] = 0

    limit = 0

    for i in range(n - 1, -1, -1):
        new = dp[:]

        for used in range(limit + 1):
            if dp[used] == -1:
                continue

            for take in range(1, m + 1):
                nd = used + take
                new[nd] = max(new[nd], dp[used] + rows[i][take])

        limit += m
        dp = new

        for used in range(limit + 1):
            if dp[used] >= v[i]:
                ans = min(ans, used)
                break

    print(ans)

for _ in range(test_cases()):
    solve()