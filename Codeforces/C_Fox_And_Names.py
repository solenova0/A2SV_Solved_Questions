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
    words = [word() for _ in range(n)]

    adj = [set() for _ in range(26)]
    indeg = [0] * 26

    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        flag = False

        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                u = ord(w1[j]) - 97
                v = ord(w2[j]) - 97
                if v not in adj[u]:
                    adj[u].add(v)
                    indeg[v] += 1
                flag = True
                break
        if not flag and len(w1) > len(w2):
            print("Impossible")
            sys.exit()

    q = deque()

    for i in range(26):
        if indeg[i] == 0:
            q.append(i)

    res = []
    while q:
        u = q.popleft()
        res.append(chr(u + 97))
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(res) != 26:
        print("Impossible")
    else:
        print("".join(res))

for _ in range(test_cases(1)):
    solve()