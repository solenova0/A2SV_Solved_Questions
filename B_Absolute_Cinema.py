for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = 0
    v = 0

    for i in range(n):
        x = a[i]
        y = b[i]
        s += max(x, y)
        v = max(v, min(x, y))

    print(s + v)