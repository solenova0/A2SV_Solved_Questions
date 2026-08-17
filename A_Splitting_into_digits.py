n = int(input())
for d in range(9, 0, -1):
    if n % d == 0:
        k = n // d
        print(k)
        print(*([d] * k))
        break