
n, m, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = sum(a)
B = sum(b)

sa = set(A - x for x in a)
sb = set(B - y for y in b)

for _ in range(q):
    x = int(input())

    flag = False

    for i in range(1, int(abs(x)**0.5) + 1):
        if x % i == 0:
            d1 = i
            d2 = x // i

            if (d1 in sa and d2 in sb) or (d2 in sa and d1 in sb):
                flag = True
                break

    print("YES" if flag else "NO")