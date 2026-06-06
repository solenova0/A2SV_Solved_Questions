from collections import deque

for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))

    indeg = [0] * n
    for v in r:
        indeg[v - 1] += 1

    q = deque()

    for i in range(n):
        if indeg[i] == 0:
            q.append(i)

    ans = 1

    while q:
        sz = len(q)

        for _ in range(sz):
            u = q.popleft()

            v = r[u] - 1
            indeg[v] -= 1

            if indeg[v] == 0:
                q.append(v)

        ans += 1

    print(ans )