n, k = map(int, input().split())
a = list(map(int, input().split()))

arr = sorted((a[i], i + 1) for i in range(n))

total = 0
res = []

for days, idx in arr:
    if total + days <= k:
        total += days
        res.append(idx)

print(len(res))
print(*res)