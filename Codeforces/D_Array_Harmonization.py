t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [1] + arr  
    a.sort()
    b.sort()
    
    i = 0
    j = 0
    match = 0
    while i < n and j < n:
        if a[i] < b[j]:
            match += 1
            i += 1
            j += 1
        else:
            j += 1
    
    op = n - match
    print(op)