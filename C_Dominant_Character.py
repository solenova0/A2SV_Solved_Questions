t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = float('inf')

    for i in range(n):
        a = b = c = 0

        for length in range(1, 8):
            if i + length > n:
                break

            ch = s[i + length - 1]
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1

            if length >= 2 and a > b and a > c:
                ans = min(ans, length)

    print(-1 if ans == float('inf') else ans)
