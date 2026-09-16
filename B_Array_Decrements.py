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

t = intinput()

for _ in range(t):
    n = intinput()
    a = listinput()
    b = listinput()

    k = -1
    ok = True

    for i in range(n):
        if b[i] > 0:
            diff = a[i] - b[i]

            if diff < 0:
                ok = False
                break

            if k == -1:
                k = diff
            elif k != diff:
                ok = False
                break

    if ok:
        if k == -1:
            k = max(a)

        for i in range(n):
            if b[i] == 0 and a[i] > k:
                ok = False
                break

    print("YES" if ok else "NO")