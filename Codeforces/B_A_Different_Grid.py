t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    if n * m == 1:
        print(-1)
        continue
    v = []
    for row in a:
        v.extend(row)

    rot = v[-1:] + v[:-1]

    for i in range(n):
        row = rot[i*m:(i+1)*m]
        print(*row)