t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    res = [p[0]]

    for i in range( 1 , n - 1):
        if p[i] < p[i - 1] and p[i] < p[i + 1]:
            res.append(p[i])

        elif p[i] > p[i - 1] and p[i] > p[i + 1]:
            res.append(p[i])
        i += 1
    res.append(p[-1])
    print(len(res))
    for j in range(len(res)):
        print(res[j], end=' ')
    print()

