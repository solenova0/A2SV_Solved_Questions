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

    freq = [0] * (n + 1)

    l = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            l += 1
        else:
            freq[l] += 1
            l = 1
    freq[l] += 1

    c = 0
    s = 0
    ans = 0

    for i in range(n, 0, -1):
        if freq[i] == 0:
            continue

        c += freq[i]
        s += i * freq[i]

        d = k - s

        if c > 0 and d % c == 0:
            x = d // c
            if i + x >= 1:
                ans += 1

    print(ans)

for _ in range(test_cases()):
    solve()