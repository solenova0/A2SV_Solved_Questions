n, k = map(int, input().split())
a = list(map(int, input().split()))
gap = a[-1] - a[0]
if k == 1:
    print(gap)
else:
    d = []
    for i in range(n - 1):
        d.append(a[i + 1] - a[i])
    
    d.sort(reverse=True)
    
    for i in range(k - 1):
        gap -= d[i]
    
    print(gap)