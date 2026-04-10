def prime(n):
    size = 10**5  
    flag = [True] * (size + 1)
    P = []
    for p in range(2, size + 1):
        if flag[p]:
            P.append(p)
            if len(P) >= n + 1:
                break
            for i in range(p * p, size + 1, p):
                flag[i] = False
    return P

t = int(input())
for _ in range(t):
    n = int(input())
    P = prime(n)
    res = []
    for i in range(n):
        res.append(P[i] * P[i+1])
    print(*res)