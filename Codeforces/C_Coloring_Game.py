t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for k in range(n-1, 1, -1):
        l = 0
        r = k - 1
        if a[k - 2] + a[k -1] < a[k]:
            ans = 0
            break
        while l < r:
            if a[l] + a[r] > a[k]:
                ans += r - l
                r -= 1
            else:
                l += 1

    print(ans)