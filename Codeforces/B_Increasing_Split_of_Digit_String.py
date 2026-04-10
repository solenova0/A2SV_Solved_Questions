q = int(input())
for _ in range(q):
    n = int(input())
    s = input()
    flag = False
    for i in range(1, n):
        a = s[:i]
        b = s[i:]
        if int(a) < int(b):
            print("YES")
            print(2)
            print(a, b)
            flag = True
            break
    if not flag:
        print("NO")