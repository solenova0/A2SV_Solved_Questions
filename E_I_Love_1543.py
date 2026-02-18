t = int(input())
target = "1543"
l = len(target)

for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    times = 0
    layers = min(n, m) // 2

    for k in range(layers):
        top, bottom = k, n - 1 - k
        left, right = k, m - 1 - k

        s = []
        # top row
        for j in range(left, right + 1):
            s.append(grid[top][j])

        # right column
        for i in range(top + 1, bottom):
            s.append(grid[i][right])

        # bottom row
        for j in range(right, left - 1, -1):
            s.append(grid[bottom][j])

        # left column
        for i in range(bottom - 1, top, -1):
            s.append(grid[i][left])

        if len(s) < l:
            continue

        s = "".join(s)
        t = s + s[:l - 1]  # handle cyclic

        for i in range(len(s)):
            if t[i:i + l] == target:
                times += 1

    print(times)
