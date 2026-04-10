def myfun(a, T):
    n = len(a)
    i = 0
    used = 0
    while i < n:
        used += 1
        start = a[i]
        while i < n and a[i] <= start + 2 * T:
            i += 1
        if used > 3:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    low, high = 0, 10**9
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        if myfun(a, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)