def solve():
    n, m, k = map(int, input().split())
    def find(mid):
        count = 0
        for i in range(1, n + 1):
            add = min(mid // i, m)
            if add == 0:
                break
            count += add
        return count < k

    low, high = 1, n * m
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        if find(mid):
            low = mid + 1
        else:
            answer = mid
            high = mid - 1

    print(answer)

t = 1
for _ in range(t):
    solve()
