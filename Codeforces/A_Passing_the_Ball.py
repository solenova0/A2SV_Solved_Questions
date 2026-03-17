t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    ans = 0
    for i in range(n-1):
        if s[i] == 'R' and s[i+1] == 'L':
            ans = i + 2
            break

    print(ans)