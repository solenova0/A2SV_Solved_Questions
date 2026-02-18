t = int(input())
for _ in range(t):
    s = input()
    valid = False
    for i in range(0,len(s) - 1):
        if s[i] == s[i + 1]:
            valid = True
            break
    if valid:
        print(1)
    else:
        print(len(s))
        
