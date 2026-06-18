n, d = map(int, input().split())
a = []

for _ in range(n):
    m, s = map(int, input().split())
    a.append((m, s))

a.sort()
l = 0
cur = 0
ans = 0

for r in range(n):
    cur += a[r][1]

    while a[r][0] - a[l][0] >= d:
        cur -= a[l][1]
        l += 1

    ans = max(ans, cur)

print(ans)