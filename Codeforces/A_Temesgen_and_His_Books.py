t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxx = 0
    for v in a[:-1]:
        maxx = max(maxx, v + a[-1])

    print(maxx)