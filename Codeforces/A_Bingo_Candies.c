t = int(input())
for _ in range(t):
    n = int(input())
    
    freq = {}
    
    for _ in range(n):
        row = list(map(int, input().split()))
        for x in row:
            freq[x] = freq.get(x, 0) + 1
    
    ok = True
    limit = n * (n - 1)
    
    for v in freq.values():
        if v > limit:
            ok = False
            break
    
    print("YES" if ok else "NO")