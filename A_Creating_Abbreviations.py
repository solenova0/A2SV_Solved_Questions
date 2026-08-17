t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    words = [input().strip() for _ in range(n)]
    abbr = [input().strip() for _ in range(m)]

    avlbl = set(word[0].upper() for word in words)

    created = [False] * m
    count = 0

    while True:
        changed = False

        for i in range(m):
            if created[i]:
                continue

            s = abbr[i]

            if all(c in avlbl for c in s):
                created[i] = True
                count += 1

                avlbl.add(s[0])
                changed = True

        if not changed:
            break

    print("YES" if count == m else "NO")