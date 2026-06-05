n = int(input())
a = list(map(int, input().split()))

if n >1:
    print(1, n)
    for i in range(n):
        print(-a[i] * n, end=" ")
        a[i] -= a[i] * n
    print()

    print(1, n - 1)
    for i in range(n - 1):
        print(-a[i], end=" ")
        a[i] = 0
    print()

    print(n ,n)
    print(-a[n-1], end=" ")
    a[n-1] = 0
    print()
else:
    print(1, 1)
    print(-a[0], end=" ")
    print()
    print(1, 1)
    print(0, end=" ")
    print()
    print(1, 1)
    print(0, end=" ")
    print()