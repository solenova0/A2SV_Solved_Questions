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
    res = []  
    while True:
        flag = True
        for i in range(n):
            if a[i] != i:
                flag= False
                break
        if flag:
            break
            
        s = set(a)
        mex = 0
        while mex in s:
            mex += 1
            
        if mex < n:
            res.append(mex + 1) 
            a[mex] = mex
        else:
            for i in range(n):
                if a[i] != i:
                    res.append(i + 1)
                    a[i] = mex
                    break
    #print(a)
    print(len(res))
    print(*res)

for _ in range(test_cases()):
    solve()