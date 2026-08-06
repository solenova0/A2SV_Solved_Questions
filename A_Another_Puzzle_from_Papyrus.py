for _ in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = sum(a) - sum(b)

    if diff < 0:
        print(-1)
        continue

    inf = 10 ** 18
    ans = inf

    flag = True
    for x, y in zip(a, b):
        if x < y:
            flag = False
            break
    if flag:
        ans = diff

    sa = sorted(a)
    sb = sorted(b)

    flag = True
    for x, y in zip(sa, sb):
        if x < y:
            flag = False
            break
    if flag:
        ans = min(ans, diff + c)

    print(ans if ans != inf else -1)