
from math import isqrt

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

    if x == 0:
        flag = 0 in sa or 0 in sb
    else:
        limit = isqrt(abs(x))
        for i in range(1, limit + 1):
            if abs(x) % i == 0:
                d1 = i
                d2 = abs(x) // i

                if x > 0:
                    if (
                        (d1 in sa and d2 in sb)
                        or (d2 in sa and d1 in sb)
                        or (-d1 in sa and -d2 in sb)
                        or (-d2 in sa and -d1 in sb)
                    ):
                        flag = True
                        break
                else:
                    if (
                        (d1 in sa and -d2 in sb)
                        or (-d2 in sa and d1 in sb)
                        or (d2 in sa and -d1 in sb)
                        or (-d1 in sa and d2 in sb)
                    ):
                        flag = True
                        break

    print("YES" if flag else "NO")