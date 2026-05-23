res = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l = 1
    r = 2 * n
    ans = 1

    while l <= r:
        mid = (l + r) // 2

        x = 0
        y = 0
        flag = False

        for i in range(n):
            v = (a[i] >= mid) + (b[i] >= mid) - 1

            if v == 1:
                x += 1
                flag = False
            elif v == -1:
                if not flag:
                    y += 1
                    flag = True

        if x > y:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    res.append(ans)

for v in res:
    print(v)