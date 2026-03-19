t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    stack = []
    stack.append(a[0])
    for v in a[1:]:
        if v >= stack[-1]:
            stack.append(v)
    print(len(stack))   

  