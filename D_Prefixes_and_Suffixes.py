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
    s1 = strinput()
    s2 = strinput()

    cnt = Counter()

    for i in range(n):
        a = s1[i]
        b = s2[n - 1 - i]

        if a > b:
            a, b = b, a

        cnt[a + b] += 1

    odd = 0
    possible = True

    for pair, count in cnt.items():
        if count % 2 == 1:
            if pair[0] != pair[1]:
                possible = False
                break

            odd += 1

    if odd > 1:
        possible = False

    if n % 2 == 0 and odd > 0:
        possible = False

    print("YES" if possible else "NO")
