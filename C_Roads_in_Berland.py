n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(n):
    for j in range(i + 1, n):
        total += dist[i][j]

k = int(input())
ans = []

for _ in range(k):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    for i in range(n):
        for j in range(i + 1, n):
            new_d = min(
                dist[i][j],
                dist[i][a] + c + dist[b][j],
                dist[i][b] + c + dist[a][j]
            )

            if new_d < dist[i][j]:
                total -= dist[i][j] - new_d
                dist[i][j] = dist[j][i] = new_d

    ans.append(str(total))

print(*ans)