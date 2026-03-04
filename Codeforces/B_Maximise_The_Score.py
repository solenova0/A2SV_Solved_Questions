t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    a.sort()
    i = 0
    while i < 2*n:
        ans += a[i]
        i += 2
    print(ans)