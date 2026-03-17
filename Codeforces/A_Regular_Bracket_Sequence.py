t = int(input())
for _ in range(t):
    s = input()
    
    if len(s) % 2 == 1:
        print("NO")
        continue

    stack1 = []
    stack2 = []
    ok = True

    for i, ch in enumerate(s):
        if ch == "(":
            stack1.append(i)

        elif ch == "?":
            stack2.append(i)

        else:
            if stack1:
                stack1.pop()
            elif stack2:
                stack2.pop()
            else:
                ok = False
                break

    if not ok:
        print("NO")
        continue

    while stack1 and stack2:
        if stack1[-1] < stack2[-1]:  # important check
            stack1.pop()
            stack2.pop()
        else:
            break

    if stack1:
        print("NO")
    else:
        print("YES")