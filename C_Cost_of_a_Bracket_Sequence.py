t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    matched = [False] * n
    stack = []  

    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else: 
            if len(stack) > 0:
                pos = stack.pop()
                matched[pos] = True  # this '(' is matched
                matched[i] = True           # this ')' is matched

    idx = []
    for i in range(n):
        if matched[i]:
            idx.append(i)

    removed = [False] * n
    removals = min(k, len(idx))

    for i in range(removals):
        removed[idx[i]] = True

    ans = ""
    for i in range(n):
        if removed[i]:
            ans += "1"
        else:
            ans += "0"

    print(ans)