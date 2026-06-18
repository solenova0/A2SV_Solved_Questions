for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    curr = a[0]
    for x in a[1:]:
        if x < curr:
            curr += x
        else:
            curr = x

    print(curr)