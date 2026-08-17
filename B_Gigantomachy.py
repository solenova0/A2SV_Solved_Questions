t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if b[0] + m <= a[0] + n:
        print(1)
    else:
        print(2)