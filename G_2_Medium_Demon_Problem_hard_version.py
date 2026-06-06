from collections import deque

for _ in range(int(input())):
    n = int(input())
    r = [x - 1 for x in map(int, input().split())]

    indeg = [0] * n
    for v in r:
        indeg[v] += 1

    q = deque()
    sz = [1] * n

    for i in range(n):
        if indeg[i] == 0:
            q.append(i)

    ans = 1

    while q:
        u = q.popleft()

        ans = max(ans, sz[u])

        p = r[u]
        sz[p] += sz[u]

        indeg[p] -= 1
        if indeg[p] == 0:
            q.append(p)

    print(ans)