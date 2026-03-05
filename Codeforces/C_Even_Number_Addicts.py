import sys
sys.setrecursionlimit(10000) 

u = [[[0 for _ in range(2)] for _ in range(111)] for _ in range(111)]
dp = [[[0 for _ in range(2)] for _ in range(111)] for _ in range(111)]

def go(x, y, z):
    if x + y == 0:
        return z == 0
    if u[x][y][z]:
        return dp[x][y][z]
    u[x][y][z] = 1
    res = 0
    if x > 0:
        res |= 1 - go(x - 1, y, (z + y + 1) % 2)
    if y > 0:
        res |= 1 - go(x, y - 1, (z + y + 1) % 2)
    dp[x][y][z] = res
    return res

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = sum(1 for e in a if e % 2 == 0)  
    y = n - x  
    for i in range(x + 1):
        for j in range(y + 1):
            u[i][j][0] = u[i][j][1] = 0
    res = go(x, y, 0)
    print("Alice" if res else "Bob")

t = int(input())
for _ in range(t):
    solve()