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
    enemy = list(word())
    dawit = word()
    # print(enemy)

    ans = 0
    for j in range(n):
        if dawit[j] == '1':
            if j > 0 and enemy[j - 1] == '1':
                ans += 1
                enemy[j - 1] = '0'
            elif enemy[j] == '0':
                ans += 1
                enemy[j] = '0'
            elif j < n - 1 and enemy[j + 1] == '1':
                ans += 1
                enemy[j + 1] = '0'

    print(ans)
for _ in range(test_cases()):
    solve()