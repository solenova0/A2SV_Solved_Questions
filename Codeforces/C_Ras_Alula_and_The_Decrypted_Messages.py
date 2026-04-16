t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    w = input()
    target = 0
    curr = 0
    for i in range(m):
        target += ord(w[i])
        curr += ord(s[i])
    
    flag = False
    for i in range(m, n):
        if curr == target:
            flag = True
            break
        curr += ord(s[i])
        curr -= ord(s[i - m])
    
    if flag:
        print("YES")
    else:
        print("NO")