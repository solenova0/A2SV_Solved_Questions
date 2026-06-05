from collections import deque
n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n + 1)]
edge = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

    edge[u][v] = True
    edge[v][u] = True

def bfs(start):
    dist = [-1] * (n + 1)

    q = deque([start])
    dist[start] = 0

    while q:
        node = q.popleft()

        for nxt in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                q.append(nxt)

    return dist

distS = bfs(s)
distT = bfs(t)

shortest = distS[t]

ans = 0

for u in range(1, n + 1):
    for v in range(u + 1, n + 1):

        if edge[u][v]:
            continue

        path1 = distS[u] + 1 + distT[v]
        path2 = distS[v] + 1 + distT[u]

        if min(path1, path2) >= shortest:
            ans += 1

print(ans)