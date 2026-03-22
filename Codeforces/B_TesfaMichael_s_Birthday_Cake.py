n, k = map(int, input().split())
s = input().strip()
weight = sorted(ord(c) - ord('a') + 1 for c in s)

ans = 0
temp = -float('inf')
count = 0

for w in weight:
    if w >= temp + 2:
        ans += w
        temp = w
        count += 1
        if count == k:
            break

if count < k:
    print(-1)
else:
    print(ans)