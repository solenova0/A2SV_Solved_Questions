for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    dp = [float('-inf')] * 4
    dp[0] = 0

    choice = [[0] * 4 for _ in range(n + 1)]

    for i in range(n, 0, -1):
        ndp = [float('-inf')] * 4

        for s in range(4):
            if dp[s] == float('-inf'):
                continue

            f = s >> 1
            h = s & 1

            val = a[i] if f == 0 else -a[i]

            # don't take
            if dp[s] + val > ndp[s]:
                ndp[s] = dp[s] + val
                choice[i][s] = s << 1

            # take
            if h or a[i] > 0:
                nf = f ^ 1
                ns = (nf << 1) | 1

                val2 = a[i] if nf == 0 else -a[i]

                if dp[s] + val2 > ndp[ns]:
                    ndp[ns] = dp[s] + val2
                    choice[i][ns] = (s << 1) | 1

        dp = ndp

    best = max(range(4), key=lambda x: dp[x])

    ops = []
    cur = best

    for i in range(1, n + 1):
        x = choice[i][cur]

        take = x & 1
        prev = x >> 1

        if take:
            ops.append(i)

        cur = prev

    ops = ops[::-1]

    if not ops:
        print(0)
        print()
        continue

    head = ops[0]
    tail = []

    for x in ops[1:]:
        if a[x] > 0:
            tail.append(head)
            head = x
        else:
            tail.append(x)

    ans = [head] + tail[::-1]

    print(len(ans))
    print(*ans)

