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
    first_one = -1
    last_one = -1
    for i in range(n):
        if a[i] == 1:
            if first_one == -1:
                first_one = i
            last_one = i
    if first_one == -1:
        first_minus = -1
        last_minus = -1
        for i in range(n):
            if a[i] == -1:
                if first_minus == -1:
                    first_minus = i
                last_minus = i
        if first_minus != -1:
            a[first_minus] = 1
            a[last_minus] = 1
        for i in range(first_minus + 1, last_minus):
            if a[i] == -1:
                a[i] = 0
    else:
        for i in range(first_one):
            if a[i] == -1:
                a[i] = 0

        for i in range(first_one - 1, -1, -1):
            if a[i] == -1:
                a[i] = 1
                break

        for i in range(last_one + 1, n):
            if a[i] == -1:
                a[i] = 0

        for i in range(n - 1, last_one, -1):
            if a[i] == -1:
                a[i] = 1
                break
            
        for i in range(first_one + 1, last_one):
            if a[i] == -1:
                a[i] = 0

    print(*a)

for _ in range(test_cases()):
    solve()