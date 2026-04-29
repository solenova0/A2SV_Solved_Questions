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
    deg = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1

    count = Counter(deg[1:])
    leafs = count[1]
    x = (n - leafs) - 1
    y = leafs // x

    print(x, y)


for _ in range(test_cases()):
    solve()