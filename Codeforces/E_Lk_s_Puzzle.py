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
    visited = [[False]*m for _ in range(n)]

    def dfs(x, y, px, py, color):
        visited[x][y] = True

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == color:
                    if visited[nx][ny] and not (nx == px and ny == py):
                        return True
                    if not visited[nx][ny]:
                        if dfs(nx, ny, x, y, color):
                            return True

        return False
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if dfs(i, j, -1, -1, grid[i][j]):
                    print("Yes")
                    exit()

    print("No")

for _ in range(test_cases(1)):
    solve()