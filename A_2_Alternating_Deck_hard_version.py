t = int(input())
for _ in range(t):
    n = int(input())
    aw = ab = bw = bb = 0
    step = 1
    curr = "Alice"
    count = 0
    next_white = True  

    while n > 0:
        v = min(step, n)

        if next_white:
            white = (v + 1) // 2
            black = v // 2
        else:
            white = v // 2
            black = (v + 1) // 2

        if curr == "Alice":
            aw += white
            ab += black
        else:
            bw += white
            bb += black

        if v % 2 == 1:
            next_white = not next_white

        n -= v
        step += 1
        count += 1

        if step == 2:
            curr = "Bob"
            count = 0
            continue

        if count == 2:
            curr = "Alice" if curr == "Bob" else "Bob"
            count = 0

    print(aw, ab, bw, bb)
