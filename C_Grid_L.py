t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    S = p + 2 * q
    T = 2 * S + 1
    ans = 0

    d = 1
    while d * d <= T:
        if T % d == 0:
            e = T // d

            if d % 2 == 1 and e % 2 == 1:
                n = (d - 1) // 2
                m = (e - 1) // 2

                if n > 0 and m > 0:
                    V = n * (m + 1)
                    H = m * (n + 1)

                    if q <= min(V, H):
                        ans = (n, m)
                        break

                n = (e - 1) // 2
                m = (d - 1) // 2

                if n > 0 and m > 0:
                    V = n * (m + 1)
                    H = m * (n + 1)

                    if q <= min(V, H):
                        ans = (n, m)
                        break
        d += 1

    if ans == 0:
        print(-1)
    else:
        print(ans[0], ans[1])