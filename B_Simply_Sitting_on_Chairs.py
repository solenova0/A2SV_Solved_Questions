t = int(input())
res = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    count = 0
    for i in range(1, n + 1):
        val = p[i - 1]
        if val > i:
            count += 1

    res.append(str(n - count))

for v in res:
        print(v)
