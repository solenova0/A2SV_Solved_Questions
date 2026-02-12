t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    move = [1 if c == 'R' else -1 for c in s]

    #first hit from starting position
    pos = x
    first_hit = -1
    for i, m in enumerate(move):
        pos += m
        if pos == 0:
            first_hit = i + 1
            break

    if first_hit == -1 or first_hit > k:
        print(0)
        continue

    ans = 1
    remaining = k - first_hit

    #cycle length from zero
    pos = 0
    cycle = -1
    for i, m in enumerate(move):
        pos += m
        if pos == 0:
            cycle = i + 1
            break

    if cycle != -1:
        ans += remaining // cycle

    print(ans)
