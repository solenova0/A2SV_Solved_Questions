import sys, math, itertools, heapq
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from functools import cmp_to_key
from operator import itemgetter
from random import randint

input = sys.stdin.readline

intinput = lambda: int(input())
strinput = lambda: input().strip()
listinput = lambda: list(map(int, input().split()))
tupleinput = lambda: tuple(map(int, input().split()))
mapinput = lambda: map(int, input().split())
matrixintinput = lambda n: [listinput() for _ in range(n)]
matrixstrinput = lambda n: [input().split() for _ in range(n)]

num, arr, word = intinput, listinput, strinput
words = lambda: input().split()

yn = lambda c: "YES" if c else "NO"

RANDOM = randint(1, 2**32 - 1)
xor = lambda x: x ^ RANDOM

test_cases = lambda d=0: intinput() if d == 0 else d

INF = -10**9
ans = []


def solve():
    n = intinput()
    s = strinput()

    zeros = s.count('0')
    ones = n - zeros

    best = INF

    for start in (0, 1):
        dp = [None, None]

        for ch in s:
            new = dp[:]
            cur = int(ch)

            if cur == start and dp[cur] is None:
                if cur == 0:
                    new[cur] = (1, 0)
                else:
                    new[cur] = (0, 1)

            if dp[cur ^ 1] is not None:
                keep0, keep1 = dp[cur ^ 1]

                if cur == 0:
                    nxt = (keep0 + 1, keep1)
                else:
                    nxt = (keep0, keep1 + 1)

                if new[cur] is None or nxt[0] + nxt[1] > new[cur][0] + new[cur][1]:
                    new[cur] = nxt

            dp = new
        for state in dp:
            if state is None:
                continue

            keep0, keep1 = state

            del0 = zeros - keep0
            del1 = ones - keep1

            if abs(del0 - del1) <= 1:
                best = max(best, keep0 + keep1)
    if best == INF:
        ans.append("-1")
    else:
        ans.append(str(n - best))

for _ in range(test_cases()):
    solve()

print("\n".join(ans))