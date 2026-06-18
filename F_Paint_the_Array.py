import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # mismatch array for each window
    bad = [0] * (n - m + 1)

    cur = 0

    # first window
    for i in range(m):
        if a[i] != i + 1:
            cur += 1
    bad[0] = cur

    for l in range(1, n - m + 1):
        if a[l - 1] != 1:
            cur -= 1
        if a[l + m - 1] != m:
            cur += 1
        bad[l] = cur

    # dp greedy coverage idea
    covered = [0] * n

    for l in range(n - m + 1):
        if bad[l] == 0:
            for i in range(l, l + m):
                covered[i] = 1

    ans = sum(1 for x in covered if x == 0)

    print(ans)