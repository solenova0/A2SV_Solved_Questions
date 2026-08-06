t = int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(1, n):
        a[i] += a[i - 1]

    for i in range(1, n):
        b[i] += b[i - 1]

    ok = True
    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break

    if ok:
        print("YES")
    else:
        print("NO")