t = int(input())
for _ in range(t):
    n = int(input())
    if (n // 2 ) % 2 == 0:
        print("YES")
        i = 2
        while i <= n:
            print(i)
            i += 2
        j = 1
        while i <= n + 3:
            if i != n + 1:
                print(i)
            j += 2
    else:
        print("NO")
