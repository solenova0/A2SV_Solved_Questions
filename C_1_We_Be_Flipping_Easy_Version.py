for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ops = []
    flp = 0

    for i in range(n - 1, -1, -1):
        val = a[i]

        if flp % 2:
            val = -val

        if val > 0:
            ops.append(i + 1)
            flp ^= 1

    print(len(ops))
    if ops:
        print(*ops)
    else:
        print()