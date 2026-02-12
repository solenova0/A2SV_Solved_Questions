t = int(input())
for _ in range(t):
    s = input()
    valid = False
    
    for i in range(1, len(s)):
        if s[i] != '0':   
            a = int(s[:i])
            b = int(s[i:])
            if a < b:
                print(a, b)
                valid = True
                break

    if not valid:
        print(-1)
