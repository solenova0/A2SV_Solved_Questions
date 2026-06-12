t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    mx = 1
    cur = 1

    for i in range(1, n):
        if a[i] == a[i - 1]:
            cur += 1
        else:
            mx = max(mx, cur)
            cur = 1

    mx = max(mx, cur)

    print("YES" if mx < m else "NO")