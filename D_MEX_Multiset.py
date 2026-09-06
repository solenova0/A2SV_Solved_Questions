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

    count = a.count(0)
    if count == 1:
        print("NO")
        return
 
    res = [-1] * n 
    if count == 0:
        for i in range(n):
            res[i] = 'C'
    else:
        first = True 
        for i in range(n):
            if not count: 
                break
            if a[i] == 0: 
                if first:
                    res[i] = 'A'
                else:
                    res[i] = 'B' 
                first = False
                count -= 1
 
        for i in range(n):
            if res[i] == -1: 
                res[i] = 'C'
 
    print("YES")
    print("".join(res))

for _ in range(test_cases()):
    solve()