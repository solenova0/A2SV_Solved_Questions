t = int(input())  
for _ in range(t):
    n, m, v = map(int, input().split())  
    a = list(map(int, input().split()))  
    pref = [0] * (n + 1) 
    s = cnt = 0
    for i in range(n):
        s += a[i]
        if s >= v:
            cnt += 1
            s = 0  
        pref[i + 1] = cnt

    suff = [0] * (n + 1)  
    s = cnt = 0
    for i in range(n - 1, -1, -1):
        s += a[i]
        if s >= v:
            cnt += 1
            s = 0
        suff[i] = cnt

    if pref[n] < m:
        print(-1)
        continue  
    ps = [0] * (n + 1)
    for i in range(n):
        ps[i + 1] = ps[i] + a[i]
    ans = 0
    r = 0
    for l in range(n + 1):
        r = max(r, l)  
        while r <= n and pref[l] + suff[r] >= m:
            ans = max(ans, ps[r] - ps[l])  
            r += 1

    print(ans)