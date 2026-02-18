t = int(input())
for _ in range(t):
    n = int(input())
    grid = [input() for _ in range(n)]

    operations = 0

    for i in range(n//2):
        for j in range(i, n - i - 1):
            count = [0, 0]
            count[int(grid[i][j])] += 1
            count[int(grid[j][n - 1 - i])] += 1
            count[int(grid[n - 1 - i][n - 1 - j])] += 1
            count[int(grid[n - 1 - j][i])] += 1

            operations += min(count)

    print(operations)
