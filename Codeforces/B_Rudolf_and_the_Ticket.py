import bisect
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = sorted(map(int, input().split()))
    ans = 0
    for x in b:
        ans += bisect.bisect_right(c, k - x)
    
    print(ans)