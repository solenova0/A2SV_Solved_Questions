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

num, arr, word = intinput, listinput, strinput
words = lambda: input().split()

yn = lambda c: "YES" if c else "NO"

test_cases = lambda d=0: intinput() if d == 0 else d

def solve():
    x, y = mapinput()
    s = x + y
    x_prime = 0

    for bit in range(29, -1, -1):
        value = 2 ** bit

        if s // value % 2 == 1:
            if x_prime + value <= x:
                x_prime += value

    print(s, x - x_prime)

for _ in range(test_cases()):
    solve()