t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    L, R = 0, 10**9
    for i in range(n - 1):
        if a[i] == a[i+1]:
            continue

        s = a[i] + a[i+1]

        if a[i] < a[i+1]:
            R = min(R, s // 2)
        else:
            L = max(L, (s + 1) // 2)

    if L <= R :
        print(L)
    else:
        print(-1)