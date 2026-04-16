import math
t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))
    stack = [(10**18, p[0])]
    ans = 0
    for i in range(1, n):
        hp = h[i]
        tm = 0

        while stack:
            T, P = stack[-1]
            avail = T - tm
            dmg = avail * P

            if dmg >= hp:
                break
            hp -= dmg
            tm += avail
            stack.pop()

        if not stack:
            tm += (hp + p[i] - 1) // p[i]
        else:
            T, P = stack[-1]
            tm += (hp + P - 1) // P

        stack.append((tm, p[i]))
        ans = max(ans, tm)

    print(ans)