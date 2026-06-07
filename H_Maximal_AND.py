t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for bit in range(30, -1, -1):
        count = 0

        for x in a:
            if (x >> bit) & 1:
                count += 1

        need = n - count

        if need <= k:
            k -= need
            ans |= (1 << bit)

    print(ans)