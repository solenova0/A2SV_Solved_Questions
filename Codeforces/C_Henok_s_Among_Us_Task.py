a, b = map(int, input().split())
res = [b]

while b > a:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b = (b - 1) // 10
    else:
        print("NO")
        exit()

    res.append(b)

if b == a:
    print("YES")
    res.reverse()
    print(len(res))
    print(*res)
else:
    print("NO")