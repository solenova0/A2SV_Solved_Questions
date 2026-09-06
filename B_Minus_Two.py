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
    import sys
from bisect import bisect_right

input = sys.stdin.readline


def solve():
    n = num()
    a = arr()
    odd = []
    even_even = []  
    even_odd = []   

    even_count = {}

    for x in a:
        k = x // 2
        if x % 2:
            odd.append(k)
        else:
            if k % 2 == 0:
                even_even.append(k)
            else:
                even_odd.append(k)
            even_count[k] = even_count.get(k, 0) + 1

    odd.sort()
    even_even.sort()
    even_odd.sort()
    ans = 1
    candidate = {0}

    for x in a:
        k = x // 2
        candidate.add(k)
        if k > 0:
            candidate.add(k - 1)

    for m in candidate:
        cnt_odd = bisect_right(odd, m)
        if m % 2 == 0:
            cnt_zero = bisect_right(even_even, m)
            cnt_two = bisect_right(even_odd, m)
        else:
            cnt_zero = bisect_right(even_odd, m)
            cnt_two = bisect_right(even_even, m)
        cnt_two += even_count.get(m + 1, 0)
        ans = max(ans, cnt_odd, cnt_zero, cnt_two)

    print(ans)

for _ in range(test_cases()):
    solve()