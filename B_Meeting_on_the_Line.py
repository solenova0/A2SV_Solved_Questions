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

t = intinput()
for _ in range(t):
    n = intinput()
    x = listinput()
    time = listinput()

    def check(T):
        left = -10**18
        right = 10**18

        for i in range(n):
            if T < time[i]:
                return False

            d = T - time[i]

            left = max(left, x[i] - d)
            right = min(right, x[i] + d)

            if left > right:
                return False

        return True

    lo = 0
    hi = 2 * 10**8

    while lo < hi:
        mid = (lo + hi) // 2

        if check(mid):
            hi = mid
        else:
            lo = mid + 1

    T = lo

    left = -10**18
    right = 10**18

    for i in range(n):
        d = T - time[i]
        left = max(left, x[i] - d)
        right = min(right, x[i] + d)

    print((left + right) / 2)