s = input()
stack = [-1]
maxlen = 0
for i , v in enumerate(s):
    if v == "(":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            if i - stack[-1] > maxlen:
                maxlen = i - stack[-1]
                count = 1
            elif i - stack[-1] == maxlen:
                count += 1
if maxlen == 0:
    count = 1
print(maxlen , count)

                