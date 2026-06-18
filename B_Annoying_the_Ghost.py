for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pos = [False] * n
    P = []
    flag = True

    for v in a:
        p = -1
        for j in range(n):
            if not pos[j] and b[j] >= v:
                p = j + 1
                pos[j] = True
                break

        if p == -1:
            flag = False
            break

        P.append(p)
    # print(P)

    if not flag:
        print(-1)
        continue

    ans  = 0
    for i in range(n):
        for j in range(i + 1, n):
            if P[i] > P[j]:
                ans += 1
    print(ans)
 

 