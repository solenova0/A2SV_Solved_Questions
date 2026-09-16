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

num, arr, word = intinput, listinput, strinput
words = lambda: input().split()

yn = lambda c: "YES" if c else "NO"

test_cases = lambda d=0: intinput() if d == 0 else d

def solve():
    x, y, k = mapinput()
    d = y - x
    ans = 0

    count = min(k, max(0, d - x + 1))

    for i in range(count):
        ans += d % (x + i)

    ans += (k - count) * d
    print(ans)

for _ in range(test_cases()):
    solve()