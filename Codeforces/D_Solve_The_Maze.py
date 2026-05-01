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
    grid = [list(input()) for _ in range(n)]

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    possible = True

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == 'G':
                            possible = False
                        if grid[ni][nj] == '.':
                            grid[ni][nj] = '#'

    if not possible:
        print("No")
        return

    visited = [[False] * m for _ in range(n)]
    q = deque()

    if grid[n-1][m-1] != '#':
        q.append((n-1, m-1))
        visited[n-1][m-1] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))

    flag = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G' and not visited[i][j]:
                flag = False

    print("Yes" if flag else "No")

for _ in range(test_cases()):
    solve()