t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    count = []

    if len(set(s)) == n:
        print(-1)
        continue
    p = list(range(1, n+1))
    i = 0
    while i + 1 < n:
        p[i], p[i+1] = p[i+1], p[i]
        i += 2

    print(*p)