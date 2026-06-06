import math
for _ in range(int(input())):
    k, l1, r1, l2, r2 = map(int, input().split())
    ans = 0
    p = 1

    while p <= r2:
        L = max(l1, math.ceil(l2 / p))  
        R = min(r1, r2 // p)

        if L <= R:
            ans += R - L + 1

        if p > 10**9 // k:
            break
        p *= k

    print(ans)