t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    k = n
    i = 0
    
    while i < n and p[i] == k:
        k -= 1
        i += 1
    
    if i == n:
        print(*p)
        continue
    
    r = i + p[i:].index(max(p[i:]))
    
    l, rr = i, r
    while l < rr:
        p[l], p[rr] = p[rr], p[l]
        l += 1
        rr -= 1
    
    print(*p)
