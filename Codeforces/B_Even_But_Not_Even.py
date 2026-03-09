t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    odd = []

    for d in s:
        if int(d) % 2 == 1:
            odd.append(d)

    if len(odd) >= 2:
        print(odd[0] + odd[1])
    else:
        print(-1)