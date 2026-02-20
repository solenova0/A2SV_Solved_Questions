n = int(input())
res = []

for i in range(n):
    l, r = map(int, input().split())
    res.append((l, r, i + 1))  

res.sort(key=lambda x: (x[0], -x[1]))

max_r = -1
max_idx = -1

for l, r, idx in res:
    if r <= max_r:
        print(idx, max_idx)
        break
    if r > max_r:
        max_r = r
        max_idx = idx
else:
    print(-1, -1)