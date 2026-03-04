t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    count = 0
    balanced = [False] * n

    for i in range(n):
        if a[i] == '1':
            count += 1
        else:
            count -= 1
        if count == 0:
            balanced[i] = True

    flip = False
    flag = True

    for i in range(n - 1, -1, -1):
        curr = a[i]

        if flip:
            curr = '1' if curr == '0' else '0'

        if curr != b[i]:
            if not balanced[i]:
                flag = False
                break
            flip = not flip

    print("YES" if flag else "NO")