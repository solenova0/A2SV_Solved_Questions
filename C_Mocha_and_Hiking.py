t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Case 1
    if a[-1] == 0:
        ans = list(range(1, n + 2))

    # Case 2
    elif a[0] == 1:
        ans = [n + 1] + list(range(1, n + 1))

    else:
        ans = []

        for i in range(n - 1):

            # Find 0 -> 1 transition
            if a[i] == 0 and a[i + 1] == 1:

                ans.extend(range(1, i + 2))
                ans.append(n + 1)
                ans.extend(range(i + 2, n + 1))
                break

    print(*ans)