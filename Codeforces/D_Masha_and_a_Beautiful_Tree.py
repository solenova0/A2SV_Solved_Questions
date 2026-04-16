def solve(p, l, r):
    if l == r:
        return (p[l], p[l], 0) 
    mid = (l + r) // 2

    left = solve(p, l, mid)
    right = solve(p, mid + 1, r)

    if left is None or right is None:
        return None

    lmin, lmax, lops = left
    rmin, rmax, rops = right
    if lmax < rmin:
        return (lmin, rmax, lops + rops)

    elif rmax < lmin:
        return (rmin, lmax, lops + rops + 1)

    else:
        return None


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    res = solve(p, 0, n - 1)

    if res is None:
        print(-1)
    else:
        print(res[2])