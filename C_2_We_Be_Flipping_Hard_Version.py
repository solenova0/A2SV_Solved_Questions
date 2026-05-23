inf = float('inf')
for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    dp = [0, -inf, -inf, -inf]
    choice = [[0] * 4 for _ in range(n + 1)]

    for i in range(n, 0, -1):
        new_dp = [-inf] * 4
        for s in range(4):

            if dp[s] == -inf:
                continue
            if s < 2:
                value = a[i]
            else:
                value = -a[i]

            #don't take
            if dp[s] + value > new_dp[s]:
                new_dp[s] = dp[s] + value
                choice[i][s] = s * 2  
            #  take
            can_take = (s % 2 == 1) or (a[i] > 0)

            if can_take:
                ns = (s ^ 2) | 1
                if dp[s] - value > new_dp[ns]:
                    new_dp[ns] = dp[s] - value
                    choice[i][ns] = s * 2 + 1

        dp = new_dp
    cur = max(range(4), key=lambda x: dp[x])

    ops = []

    for i in range(1, n + 1):
        if choice[i][cur] % 2 == 1:
            ops.append(i)

        cur = choice[i][cur] // 2

    ops.reverse()                  
    if len(ops) == 0: #order
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