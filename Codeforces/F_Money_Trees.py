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
    n , k = mapinput()
    a = arr()
    h = arr()
    ans = 0
    l = 0
    s = 0
    for r in range(n):
        if r > 0 and h[r - 1] % h[r] != 0:
            l = r
            s = 0

        s += a[r]
        while s > k:
            s -= a[l]
            l += 1
        ans  = max(ans, r - l + 1)
    print(ans)

for _ in range(test_cases()):
    solve()