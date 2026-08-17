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
matrixintinput = lambda n: [listinput() for _ in range(n)]
matrixstrinput = lambda n: [input().split() for _ in range(n)]

num, arr, word = intinput, listinput, strinput
words = lambda: input().split()

yn = lambda c: "YES" if c else "NO"

RANDOM = randint(1, 2**32 - 1)
xor = lambda x: x ^ RANDOM

test_cases = lambda d=0: intinput() if d == 0 else d


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    low = []
    high = []
    delayed = {}

    low_sum = 0
    high_sum = 0

    def clean_low():
        while low:
            x = -low[0]

            if delayed.get(x, 0):
                heapq.heappop(low)
                delayed[x] -= 1

                if delayed[x] == 0:
                    del delayed[x]
            else:
                break

    def clean_high():
        while high:
            x = high[0]

            if delayed.get(x, 0):
                heapq.heappop(high)
                delayed[x] -= 1

                if delayed[x] == 0:
                    del delayed[x]
            else:
                break

    def balance():
        nonlocal low_sum, high_sum

        clean_low()
        clean_high()

        while len(low) > len(high) + 1:
            x = -heapq.heappop(low)

            low_sum -= x
            high_sum += x

            heapq.heappush(high, x)

        while len(low) < len(high):
            x = heapq.heappop(high)

            high_sum -= x
            low_sum += x

            heapq.heappush(low, -x)

        clean_low()
        clean_high()

    def add(x):
        nonlocal low_sum, high_sum

        clean_low()

        if not low or x <= -low[0]:
            heapq.heappush(low, -x)
            low_sum += x
        else:
            heapq.heappush(high, x)
            high_sum += x

        balance()

    def remove(x):
        nonlocal low_sum, high_sum

        clean_low()
        clean_high()

        if low and x <= -low[0]:
            low_sum -= x
        else:
            high_sum -= x

        delayed[x] = delayed.get(x, 0) + 1

        balance()

    for i in range(k):
        add(a[i])

    ans = []

    for i in range(k, n + 1):
        clean_low()

        median = -low[0]

        left_cost = median * len(low) - low_sum
        right_cost = high_sum - median * len(high)

        ans.append(left_cost + right_cost)

        if i == n:
            break

        remove(a[i - k])
        add(a[i])

    print(*ans)


for _ in range(test_cases(1)):
    solve()