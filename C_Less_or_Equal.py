n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
if k == 0:
    if a[0] == 1:
        print(-1)
    else:
        print(1)
else:
    x = a[k - 1]
    if k < n and a[k] == x:
        print(-1)
    else:
        print(x)