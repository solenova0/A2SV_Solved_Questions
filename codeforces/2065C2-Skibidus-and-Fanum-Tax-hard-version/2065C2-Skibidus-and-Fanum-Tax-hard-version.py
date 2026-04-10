import bisect
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(map(int, input().split()))
    prev = -float('inf')
        
    for i in range(n):
        best = float('inf')
        if a[i] >= prev:
            best = a[i]
        j = bisect.bisect_left(b, prev + a[i])
        if j < m:
            best = min(best, b[j] - a[i])
            
        if best == float('inf'):
            print("NO")
            break
            
        prev = best
    else:
        print("YES")