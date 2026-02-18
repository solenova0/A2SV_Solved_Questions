t = int(input())
for _ in range(t):
    n = int(input())
    alice = 0
    bob = 0
    step = 1
    curr = "Alice"
    count = 0

    while n > 0:
        give = min(step, n)
        if curr == "Alice":
            alice += give
        else:
            bob += give

        n -= give
        step += 1
        count += 1

        if step == 2:  
            curr = "Bob"
            count = 0
            continue

        if count == 2:
            curr = "Alice" if curr == "Bob" else "Bob"
            count = 0

    print(alice, bob)
