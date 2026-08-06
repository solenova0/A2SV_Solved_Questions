for _ in range(int(input())):
    x = int(input())

    p = 1
    temp = x
    while temp > 0:
        p *= 10
        temp //= 10

    print(p + 1)