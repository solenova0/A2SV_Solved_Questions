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
    n = num()
    a = list(word())   
    b = list(word())

    T = [0] * (n + 1)

    for i in range(1, n + 1):
        x = (a[i-1] == 'B') + (b[i-1] == 'B')
        y = (a[i-1] == 'R') + (b[i-1] == 'R')

        r = T[i-1] + min(x, y)

        if i >= 2:
            x1 = (a[i-2] == 'B') + (a[i-1] == 'B')
            y1 = (a[i-2] == 'R') + (a[i-1] == 'R')
            x2 = (b[i-2] == 'B') + (b[i-1] == 'B')
            y2 = (b[i-2] == 'R') + (b[i-1] == 'R')

            r = min(r, T[i-2] + min(x1, y1) + min(x2, y2))

        T[i] = r

    print(T[n])

for _ in range(test_cases()):
    solve()