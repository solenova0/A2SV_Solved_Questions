from collections import deque
t = int(input())
for _ in range(t):
    n, k, p, m = map(int, input().split())
    a = list(map(int, input().split()))

    deck = deque([(a[i], i) for i in range(n)])
    ans = 0

    while True:
        best = float('inf')
        idx = -1
        for i in range(k):
            if deck[i][0] < best:
                best = deck[i][0]
                idx = i

        if m < best:
            break

        m -= best

        if deck[idx][1] == p-1:
            ans += 1

        card = deck[idx]
        del deck[idx]
        deck.append(card)

    print(ans)