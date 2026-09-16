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
    n = num()
    s = word()
    for cost in range(1, 4):
        curr = {0}

        for ch in s:
            nxt = set()

            for x in curr:
                if ch == '0':
                    if -cost <= x <= cost and x != 0:
                        nxt.add(0)

                elif ch == '+':
                    lo = max(1, x - cost)
                    hi = x + cost

                    nxt.update(range(lo, hi + 1))

                    if x - cost <= 0:
                        nxt.discard(0)
                else:
                    lo = x - cost
                    hi = min(-1, x + cost)

                    nxt.update(range(lo, hi + 1))

            curr = nxt

            if not curr:
                break

        if curr:
            print(cost)
            return

    print(-1)


for _ in range(test_cases()):
    solve()