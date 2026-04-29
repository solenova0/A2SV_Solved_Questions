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
        n, m = mapinput()
        a = arr()
        x = arr()     
        total = sum(a)
        
        odd = []
        even = []
        for i in range(n):
            if (i + 1) % 2 == 1:
                odd.append(a[i])
            else:
                even.append(a[i])
        
        v1 = 0  
        v2 = 0
        for xi in x:
            if xi % 2 == 1:
                v1 += 1
            else:
                v2 += 1
        
        odd.sort(reverse=True)
        even.sort(reverse=True)
        
        curr = 0
        if v1 > 0 and len(odd) > 0:
            curr += odd[0]
            limit = min(v1, len(odd))
            
            for i in range(1, limit):
                if odd[i] > 0:
                    curr += odd[i]
        
        if v2 > 0 and len(even) > 0:
            curr += even[0]
            limit = min(v2, len(even))
            
            for i in range(1, limit):
                if even[i] > 0:
                    curr += even[i]
        print(total - curr)

for _ in range(test_cases()):
    solve()