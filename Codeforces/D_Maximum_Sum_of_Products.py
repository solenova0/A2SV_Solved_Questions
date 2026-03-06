n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
summ = sum(a[i] * b[i] for i in range(n))
needs = 0

for c in range(n):
    diff = 0
    l = c - 1
    r = c + 1
    
    while l >= 0 and r < n:
        diff += a[l] * b[r] + a[r] * b[l] - a[l] * b[l] - a[r] * b[r]
        needs = max(needs, diff)
        l -= 1
        r += 1

for c in range(n - 1):
    diff = 0
    l = c
    r = c + 1
    
    while l >= 0 and r < n:
        diff += a[l] * b[r] + a[r] * b[l] - a[l] * b[l] - a[r] * b[r]
        needs = max(needs, diff)
        l -= 1
        r += 1

print(summ + needs)