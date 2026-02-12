n, m = map(int, input().split())
count = 0

if m % n != 0:
    print(-1)
else:
    x = m // n
    while x > 1:
        if x % 2 == 0:
            x //= 2
            count += 1
        elif x % 3 == 0:
            x //= 3
            count += 1
        else:
            break

    print(count if x == 1 else -1)
