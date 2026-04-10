import bisect
n, m = map(int, input().split())
res = []
summ = 0
for _ in range(n):
    x, y = map(int, input().split())
    summ += x * y
    res.append(summ)

moment = list(map(int, input().split()))
for v in moment:
    idx = bisect.bisect_left(res, v)
    print(idx + 1)