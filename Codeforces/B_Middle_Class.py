t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    total = 0
    
    for i in range(n-1, -1, -1):
        total += a[i]
        k = n - i
        
        if total / k >= x:
            count = k
        else:
            break
    print(count)