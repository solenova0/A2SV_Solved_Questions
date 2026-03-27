t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    curr = a[0]
    count = 1
    for v in a[1:]:
        if v >= curr:
            count += 1
            curr = v
    print(count)   

  