t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    mid = n // 2
    l = mid
    r = mid

    while l >= 0 and s[l] == s[mid]:
        l -= 1
    while r < n and s[r] == s[mid]:
        r += 1

    print(r - l - 1)