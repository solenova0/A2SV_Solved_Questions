from sys import setrecursionlimit
setrecursionlimit(200000)

n, m = map(int, input().split())
cats = list(map(int, input().split()))

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ans = 0

def dfs(u, p, cnt):
    global ans

    if cats[u]:
        cnt += 1
    else:
        cnt = 0

    if cnt > m:
        return

    leaf = True

    for v in g[u]:
        if v != p:
            leaf = False
            dfs(v, u, cnt)

    if leaf:
        ans += 1

dfs(0, -1, 0)
print(ans)