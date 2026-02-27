n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
curr = 0
ans = 0

for i in range(n):
    curr += a[i]
    while curr >= s:
        curr -= a[l]
        l += 1
    ans += l

print(ans)