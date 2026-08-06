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

    s1 = [0] * (n + 1)
    s2 = [0] * (n + 1)

    for i in range(1, n + 1):
        x = a[i - 1]

        s1[i] = s1[i - 1] + (1 if x == 1 else -1)
        s2[i] = s2[i - 1] + (1 if x != 3 else -1)

    inf = -10**18
    Max = [inf] * (n + 2)

    Max[n - 1] = s2[n - 1]
    for i in range(n - 2, 0, -1):
        Max[i] = max(Max[i + 1], s2[i])

    flag = False

    for i in range(1, n - 1):
        if s1[i] >= 0 and Max[i + 1] >= s2[i]:
            flag = True
            break

    if flag:
        print("YES")
        
    else:
        print("NO")

for _ in range(test_cases()):
    solve()