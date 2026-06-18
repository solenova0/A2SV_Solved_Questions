for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    pref = float('inf')
    ans = 0
    for x in a:
        pref = min(pref, x)
        ans += pref

    print(ans)