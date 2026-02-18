t = int(input())
for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))
    summ = sum(b)
    total = summ + s

    n = 1
    while n * (n + 1) // 2 < total:
        n += 1

    if n * (n + 1) // 2 != total or max(b) > n:
        print("NO")
    else:
        print("YES")
