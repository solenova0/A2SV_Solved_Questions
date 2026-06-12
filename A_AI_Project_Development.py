t = int(input())
for _ in range(t):
    n, x, y, z = map(int, input().split())
    without = (n + x + y - 1) // (x + y)

    wrtn = x * z

    if wrtn >= n:
        w = (n + x - 1) // x
    else:
        rem = n - wrtn
        speed = x + 10 * y
        extra = (rem + speed - 1) // speed
        w = z + extra

    print(min(without, w))