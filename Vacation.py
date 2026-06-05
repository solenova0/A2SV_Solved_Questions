n = int(input())
dp = [0, 0, 0]

for _ in range(n):
    a, b, c = map(int, input().split())

    ndp = [0, 0, 0]

    ndp[0] = a + max(dp[1], dp[2])
    ndp[1] = b + max(dp[0], dp[2])
    ndp[2] = c + max(dp[0], dp[1])

    dp = ndp

print(max(dp))