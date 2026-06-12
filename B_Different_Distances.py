t = int(input())
for _ in range(t):
    n = int(input())

    ans = []
    for i in range(1, n + 1):
        ans.append(i)

    for i in range(1, n + 1):
        ans.append(i)

    for i in range(2, n + 1):
        ans.append(i)
    ans.append(1)

    for i in range(1, n + 1):
        ans.append(i)
    from collections import Counter
    print(Counter(ans))
    print(*ans)