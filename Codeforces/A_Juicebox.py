t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    box = []
    for _ in range(k):
        b, c = map(int, input().split())
        box.append((b, c))

    box.sort()  
    total = []
    curr = None
    summ = 0

    for b, c in box:
        if b != curr:
            if curr is not None:
                total.append(summ)
            curr = b
            summ = c
        else:
            summ += c

    total.append(summ)
    total.sort(reverse=True)
    ans = sum(total[:n])
    print(ans)



