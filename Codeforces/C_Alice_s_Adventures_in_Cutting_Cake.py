t = int(input())
for _ in range(t):
    n, m, v = map(int, input().split())
    arr = list(map(int, input().split()))

    pref = [0]*(n+1)
    for i in range(n):
        pref[i+1] = pref[i] + arr[i]

    suf = [n]
    summ = 0
    count = 0
    for i in range(n-1,-1,-1):
        summ += arr[i]
        if summ >= v:
            count += 1
            suf.append(i)
            summ = 0

    if count < m:
        print(-1)
        continue

    pre = [0]
    summ = 0
    for i in range(n):
        summ += arr[i]
        if summ >= v:
            pre.append(i+1)
            summ = 0

    print(pre)
    print(suf)
    ans = 0
    for l in range(len(pre)):
        r = m - l
        if r < 0 or r >= len(suf):
            continue
        L = pre[l]
        R = suf[r]
        if L <= R:
            ans = max(ans, pref[R] - pref[L])
    print(ans)