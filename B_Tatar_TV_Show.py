for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    flag = True
    for r in range(k):
        cnt = 0

        for i in range(r, n, k):
            cnt += s[i] == '1'
        if cnt % 2:
            flag = False
            break
    print("YES" if flag else "NO")