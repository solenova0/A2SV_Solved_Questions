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
    a = arr()
    pref = 0
    good = []
    bad = []
    
    for i in range(n):
        pref += a[i]
        if pref >= 0:
            good.append(i)
        else:
            bad.append(i)
    
    p = [0] * n
    
    cur = n
    for i in reversed(good):
        p[i] = cur
        cur -= 1
    for i in bad:
        p[i] = cur
        cur -= 1
    
    print(*p)

for _ in range(test_cases()):
    solve()