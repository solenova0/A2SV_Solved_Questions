t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    sumr = 0
    sumb = 0
    maxr = 0
    maxb = 0   
    for v in r:
        sumr += v
        maxr = max(maxr, sumr)
    for v in b:
        sumb += v
        maxb = max(maxb, sumb)
    print(maxr + maxb)