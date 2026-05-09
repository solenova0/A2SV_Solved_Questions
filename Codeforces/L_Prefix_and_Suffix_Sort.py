def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if all(a[i] <= a[i+1] for i in range(n-1)):
        print(0)
        return

    l = 0
    while l + 1 < n and a[l] <= a[l + 1]:
        l += 1
    r = n - 1
    while r - 1 >= 0 and a[r - 1] <= a[r]:
        r -= 1

    k = min(l + 1, n - r)

    print(k)

for _ in range(int(input())):
    solve()