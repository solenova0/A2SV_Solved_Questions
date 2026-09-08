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
    n, k = mapinput()
    a = arr()
    pref = [0] * n
    pref[0] = a[0]

    for i in range(1, n):
        pref[i] = pref[i - 1] + a[i]

    b = [a[i] - i * k for i in range(n)]
    ans = [0] * n

    for i in range(1, n - 1):
        target = a[i - 1] - i * k
        lo = i + 1
        hi = n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if b[mid] > target:
                lo = mid + 1
            else:
                hi = mid - 1

        cnt = lo - i - 1

        if cnt > 0:
            sum_a = pref[lo - 1] - pref[i]
            sum_req = k * cnt * (cnt + 1) // 2
            total = a[i - 1] * cnt
            ans[i] = (sum_a - total - sum_req)

    print(*ans)

for _ in range(test_cases()):
    solve()