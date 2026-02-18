t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int , input().split()))

    if all(x == a[0] for x in a):
        print(0)
        continue

    l = 1
    while l < n and a[l] == a[0]:
        l += 1

    r = n - 1
    while r >= 0 and a[r] == a[-1]:
        r -= 1

    if a[0] == a[-1]:
        print( r - l + 1)
    else:
        print(min(n - l, r + 1))
