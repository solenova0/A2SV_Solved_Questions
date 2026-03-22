import sys
input = sys.stdin.readline

h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]

H = [[0]*w for _ in range(h)]
V = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if grid[i][j] == '.':
            if j > 0 and grid[i][j-1] == '.':
                H[i][j] = 1
            if i > 0 and grid[i-1][j] == '.':
                V[i][j] = 1

prefH = [[0]*(w+1) for _ in range(h+1)]
prefV = [[0]*(w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        prefH[i][j] = (
            prefH[i-1][j] + prefH[i][j-1] - prefH[i-1][j-1]
            + H[i-1][j-1]
        )
        prefV[i][j] = (
            prefV[i-1][j] + prefV[i][j-1] - prefV[i-1][j-1]
            + V[i-1][j-1]
        )

def get_sum(pref, r1, c1, r2, c2):
    return (
        pref[r2][c2]
        - pref[r1-1][c2]
        - pref[r2][c1-1]
        + pref[r1-1][c1-1]
    )

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    horizontal = get_sum(prefH, r1, c1+1, r2, c2) if c1 < c2 else 0

    vertical = get_sum(prefV, r1+1, c1, r2, c2) if r1 < r2 else 0

    print(horizontal + vertical)