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
    arr = listinput()

    arr.sort()

    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + arr[i])

    suffix = [0]
    for i in range(n - 1, -1, -1):
        suffix.append(suffix[-1] + arr[i])

    ans = False

    for k in range(1, n + 1):
        if 2 * k + 1 <= n:
            blue_sum = prefix[k + 1]
            red_sum = suffix[k]

            if blue_sum < red_sum:
                ans = True

    if ans:
        print("YES")
    else:
        print("NO")

