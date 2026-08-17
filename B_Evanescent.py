for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    cnt = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            cnt += 1

    ans = cnt

    for i in range(1, n - 1):
        if s[i - 1] == s[i] == s[i + 1]:
            cur = cnt
        elif s[i - 1] == s[i + 1] != s[i]:
            cur = cnt - 2
        elif s[i] != s[i - 1] and s[i] != s[i + 1]:
            cur = cnt - 1
        else:
            cur = cnt
        ans = min(ans, cur)

    print(ans)