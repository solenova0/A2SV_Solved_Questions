from collections import deque
def solve():
    n, m = map(int, input().split())
 
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
 
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        indeg[u] += 1
        indeg[v] += 1
 
    q = deque()
 
    for i in range(1, n + 1):
        if indeg[i] == 1:
            q.append(i)
 
    ans = 0
    while q:
        count = 0
 
        for _ in range(len(q)):
            v = q.popleft()
 
            if indeg[v] == 0:
                continue
 
            count = 1
 
            for nei in adj[v]:
                indeg[nei] -= 1
 
                if indeg[nei] == 1:
                    q.append(nei)
 
        ans += count
 
    print(ans)
    
for _ in range(1):
    solve()

