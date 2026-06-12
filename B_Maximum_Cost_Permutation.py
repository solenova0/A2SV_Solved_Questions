t = int(input())
for _ in range(t):  
    n = int(input())
    p = list(map(int, input().split()))
    pos0 = []
    used = [0] * n

    for i in range(n):
        p[i] -= 1

        if p[i] == -1:
            pos0.append(i)
        else:
            used[p[i]] = 1

    if len(pos0) == 1:
        unused = 0
        for i in range(n):
            if used[i] == 0:
                unused = i

        p[pos0[0]] = unused

    l = 0
    r = n - 1

    while l < n and p[l] == l:
        l += 1

    while r >= 0 and p[r] == r:
        r -= 1

    print(max(0, r - l + 1))

