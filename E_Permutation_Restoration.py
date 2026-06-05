import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    intrvls = []

    for i in range(1, n + 1):
        x = b[i - 1]

        if x == 0:
            L = i + 1
            R = n
        else:
            L = i // (x + 1) + 1
            R = i // x

        intrvls.append((L, R, i - 1))

    intrvls.sort()

    ans = [0] * n
    heap = []

    pos = 0

    for value in range(1, n + 1):

        while pos < n and intrvls[pos][0] <= value:
            L, R, idx = intrvls[pos]
            heapq.heappush(heap, (R, idx))
            pos += 1

        R, idx = heapq.heappop(heap)

        ans[idx] = value

    print(*ans)