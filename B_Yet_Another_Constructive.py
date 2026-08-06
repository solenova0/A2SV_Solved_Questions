def solve():
    n, k, m = map(int, input().split())

    if m == 1:
        if k == 1:
            print("YES")
            print(*([1] * n))
        else:
            print("NO")
        return

    if k >= m:
        print("NO")
        return

    print("YES")
    ans = []

    for _ in range(k - 1):
        ans.append(1)

    ans.append(m - k + 1)

    for i in range(k, n):
        ans.append(ans[i % k])

    print(*ans)


t = int(input())
for _ in range(t):
    solve()