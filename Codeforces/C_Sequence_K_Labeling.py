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
    p = defaultdict(list) # position
    for i in range(n):
        p[a[i]].append(i)
    for v in p:
        if len(p[v]) > k:
            print("NO")
            exit()

    print("YES")
    c = [0] * n
    curr = 1
    for v in p:
        for idx in p[v]:
            c[idx] = curr
            curr += 1
            if curr > k:
                curr = 1

    print(*c)
for _ in range(test_cases(1)):
    solve()