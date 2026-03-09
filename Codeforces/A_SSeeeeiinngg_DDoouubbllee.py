t = int(input())
for _ in range(t):
    s = input()
    s = sorted(s)
    l = "".join(s)
    r = "".join(s[::-1])
    
    print(l + r)