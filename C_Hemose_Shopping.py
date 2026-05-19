for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    b = sorted(a)
    flag = True

    for i in range(n - x, x):
        if 0 <= i < n and a[i] != b[i]:
            flag = False
            break

    print("YES" if flag else "NO")
