import sys
sys.setrecursionlimit(10**7)
for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    vis = [False] * (n + 1)
    ans = [-1] * (n + 1)

    ok = True

    for i in range(1, n + 1):
        if vis[i]:
            continue
        cyc = []
        cur = i
        while not vis[cur]:
            vis[cur] = True
            cyc.append(cur)
            cur = a[cur]

        L = len(cyc)

        pos = {cyc[j]: j for j in range(L)}

        k = None
        for x in cyc:
            if b[x] != -1:
                if b[x] not in pos:
                    ok = False
                    break
                cur_k = (pos[b[x]] - pos[x]) % L
                if k is None:
                    k = cur_k
                elif k != cur_k:
                    ok = False
                    break

        if not ok:
            break

        if k is None:
            best = 10**9
            best_k = 0

            for sh in range(L):
                val = cyc[sh]
                if val < best:
                    best = val
                    best_k = sh

            k = best_k

        for j in range(L):
            ans[cyc[j]] = cyc[(j + k) % L]

    if not ok:
        print("NO")
    else:
        print("YES")
        print(*ans[1:])