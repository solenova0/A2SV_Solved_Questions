for _ in range(int(input())):
    n = int(input())

    ans = []

    for i in range(1, n + 1):
        ans.append(2 * i - 1)

    print(*ans)