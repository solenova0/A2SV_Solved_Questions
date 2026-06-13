n, k = map(int, input().split())
a = list(map(int, input().split()))

curr = sum(a[:k])
best = curr
ans = 1
for i in range(k, n):
    curr += a[i] - a[i - k]
    if curr < best:
        best = curr
        ans = i - k + 2

print(ans)