t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    l = 0
    r = n - 1

    left_sum = 0
    right_sum = 0
    ans = 0

    while l <= r:
        if left_sum <= right_sum:
            left_sum += a[l]
            l += 1
        else:
            right_sum += a[r]
            r -= 1

        if left_sum == right_sum:
            ans = l + (n - 1 - r)

    print(ans)