import sys
input = sys.stdin.readline
def solve():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1

    arr = list(map(int, input().split()))

    a = []
    b = []

    for i in range(n):
        if i <= x or i > y:
            a.append(arr[i])
        else:
            b.append(arr[i])

    if b:
        pos = b.index(min(b))
        b = b[pos:] + b[:pos]

    m = b[0] if b else -1

    i = 0
    while i < len(a) and a[i] < m:
        i += 1

    a = a[:i] + b + a[i:]

    print(*a)


t = int(input())
for _ in range(t):
    solve()