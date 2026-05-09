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
    input() 
    n, k  = mapinput()
    friends = arr()
    g = [[] for _ in range(n + 1)]
        
    for _ in range(n - 1):
        u, v = mapinput()
        g[u].append(v)
        g[v].append(u)
        
    distance = [-1] * (n + 1)
    q = deque()
        
    for f in friends:
        distance[f] = 0
        q.append(f)
        
    while q:
        u = q.popleft()
        for v in g[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                q.append(v)
        
    vlid = [-1] * (n + 1)
    q = deque([1])
    vlid[1] = 0
        
    while q:
        u = q.popleft()
        for v in g[u]:
            if vlid[v] == -1:
                vlid[v] = vlid[u] + 1
                q.append(v)
        
        #  leaf node check
    flag = False
    for i in range(2, n + 1):
        if len(g[i]) == 1: 
            if vlid[i] < distance[i]:
                flag = True
                break
    print("YES" if flag else "NO")

for _ in range(test_cases()):
    solve()