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
    s = input()
    
    blocks = []
    count = 0
    
    for c in s:
        if c == 'A':
            count += 1
        else:
            if count > 0:
                blocks.append(count)
            count = 0
    if count > 0:
        blocks.append(count)
    
    if len(blocks) <= 1:
        print(0)
    else:
        blocks.sort()
        print(sum(blocks[1:]))

for _ in range(test_cases()):
    solve()