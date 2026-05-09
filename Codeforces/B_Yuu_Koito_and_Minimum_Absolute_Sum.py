t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1, n - 1):
        if a[i] == -1:
            a[i] = 0
    if a[0] == -1 and a[-1] == -1:
        a[0] = a[-1] = 0
    elif a[0] == -1:
        a[0] = a[-1]
    elif a[-1] == -1:
        a[-1] = a[0]

    ans = abs(a[-1] - a[0])
    print(ans)
    print(*a)

