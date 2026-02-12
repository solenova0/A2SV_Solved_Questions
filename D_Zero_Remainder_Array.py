t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    needs = []
    for ai in a:
        need = (k - ai % k) % k
        if need != 0:
            needs.append(need)

    if not needs:
        print(0)
        continue

    needs.sort()

    max_last = -1
    i = 0
    m = len(needs)

    while i < m:
        j = i
        while j < m and needs[j] == needs[i]:
            j += 1

        val = needs[i]
        cnt = j - i

        last_x = val + k * (cnt - 1)
        max_last = max(max_last, last_x)

        i = j

    print(max_last + 1)