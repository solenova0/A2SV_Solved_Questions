import math
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    if sum(a) > k:
        print(-1)
        continue

    def myfun(s):
        v = 0
        for i in range(n):
            v += math.ceil(d[i]/s)*a[i]
        return v <= k

    low = 1
    high = max(d)
    while low <= high:
        mid = low + (high - low)//2
        if myfun(mid):
            high = mid - 1
        else:
            low = mid + 1
    print(low)