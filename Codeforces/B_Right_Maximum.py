t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    stack = []
    for v in a[-1]:
        while stack and stack[-1] > v:
            stack.pop()
        stack.append(v)
    print(len(stack))   

  