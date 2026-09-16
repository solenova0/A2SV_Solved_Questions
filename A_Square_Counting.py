import sys, math, itertools, heapq
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from functools import cmp_to_key
from operator import itemgetter
from random import randint

input = sys.stdin.readline

intinput = lambda: int(input())
strinput = lambda: input().strip()
listinput = lambda: list(map(int, input().split()))
tupleinput = lambda: tuple(map(int, input().split()))
mapinput = lambda: map(int, input().split())

t = intinput()

for _ in range(t):
    n, s = mapinput()

    print(s // (n * n))
