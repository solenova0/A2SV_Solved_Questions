from bisect import bisect_left
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    used = [False] * (n + 1)

    import heapq
    pq = list(range(1, n + 1))
    heapq.heapify(pq)

    b = []

    for x in a:
        if not used[x]:
            b.append(x)
            used[x] = True
        else:
            while used[pq[0]]:
                heapq.heappop(pq)

            y = heapq.heappop(pq)
            used[y] = True
            b.append(y)

    print(*b)