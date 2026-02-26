n = 8
if (n // 2 ) % 2 == 0:
    print("YES")
    i = 2
    while i <= n:
        print(i)
        i += 2
    j = 1
    while j <= n + 3:
        if j != n + 1:
            print(j)
        j += 2
else:
    print("NO")