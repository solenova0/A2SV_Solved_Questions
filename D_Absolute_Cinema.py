t = int(input())

for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))
    
    a = [0] * n
    
    # special case for n=2
    if n == 2:
        a[0] = f[1]
        a[1] = f[0]
        print(*a)
        continue
    
    # For n>=3
    # Using the formula a1 = (f2 - f1 + fn - f(n-1)) / 2
    # Then we can compute remaining using differences
    a[0] = (f[1] - f[0] + f[-1] - f[-2]) // 2
    
    for i in range(1, n):
        a[i] = f[i] - sum(a[:i])
    
    print(*a)
