t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mx = a[-1]
    ans = 0

    for k in range(2, n):
        l = 0
        r = k - 1
        
        while l < r:
            if a[l] + a[r] > a[k] and a[l] + a[r] + a[k] > mx:
                ans += r - l
                r -= 1
            else:
                l += 1

    print(ans)