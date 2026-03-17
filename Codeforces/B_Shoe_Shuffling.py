t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    p = list(range(1, n + 1))  
    l = 0
    flag = True

    while l < n:
        r = l
        while r < n - 1 and s[r] == s[r + 1]:
            r += 1
        if l == r:
            flag = False
            break
        temp = p[l:r+1]
        temp = temp[1:] + temp[:1]
        p[l:r+1] = temp

        l = r + 1

    if flag:
        print(*p)
    else:
        print(-1)