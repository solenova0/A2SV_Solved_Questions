n, k, q = map(int, input().split())

MAX = 200000

diff = [0]*(MAX+2)

for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r+1] -= 1

cover = [0]*(MAX+1)

cur = 0
for i in range(1, MAX+1):
    cur += diff[i]
    cover[i] = cur

good = [0]*(MAX+1)

for i in range(1, MAX+1):
    if cover[i] >= k:
        good[i] = 1

pref = [0]*(MAX+1)

for i in range(1, MAX+1):
    pref[i] = pref[i-1] + good[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(pref[b] - pref[a-1])