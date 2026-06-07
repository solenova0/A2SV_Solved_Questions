INF = 10**18
s = input().strip()
t = input().strip()

if len(s) != len(t):
    print(-1)
    exit()

n = int(input())
dist = [[INF] * 26 for _ in range(26)]

for i in range(26):
    dist[i][i] = 0

for _ in range(n):
    a, b, w = input().split()
    w = int(w)

    x = ord(a) - ord('a')
    y = ord(b) - ord('a')

    dist[x][y] = min(dist[x][y], w)

# Floyd-Warshall
for k in range(26):
    for i in range(26):
        for j in range(26):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
ans_cost = 0
ans_string = []

for a, b in zip(s, t):
    x = ord(a) - ord('a')
    y = ord(b) - ord('a')

    best_cost = INF
    best_char = -1

    for c in range(26):
        cur = dist[x][c] + dist[y][c]

        if cur < best_cost:
            best_cost = cur
            best_char = c

    if best_cost >= INF:
        print(-1)
        exit()

    ans_cost += best_cost
    ans_string.append(chr(best_char + ord('a')))

print(ans_cost)
print("".join(ans_string))