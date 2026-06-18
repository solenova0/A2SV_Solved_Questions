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
    s = word()

    freq = [1, 0, 0]  
    pref = 0
    A = 0  
    for ch in s:
        if ch == '0':
            pref = (pref + 1) % 3
        else:
            pref = (pref - 1) % 3

        A += freq[pref]
        freq[pref] += 1

    B = 0   
    both = 0  
    l = 0
    while l < n:
        r = l
        while r + 1 < n and s[r] != s[r + 1]:
            r += 1

        L = r - l + 1
        B += L * (L - 1) // 2

        a = L // 2
        b = L - a
        both += a * b
        l = r + 1
    # print(A, B, both)
    bad = A + B - both
    total = n * (n + 1) // 2
    ans = total - bad

    print(ans)
    # print()

for _ in range(test_cases()):
    solve()


