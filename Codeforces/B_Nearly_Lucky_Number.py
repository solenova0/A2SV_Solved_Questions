n = input()
count = 0
for d in n:
    if d == '4' or d == '7':
        count += 1
if set(str(count)) <= {'4', '7'} and count > 0:
    print("YES")
else:
    print("NO")