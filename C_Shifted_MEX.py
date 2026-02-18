t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    s = sorted(set(a))
    
    maxx = 1
    curr = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1] + 1:
            curr += 1
            maxx = max(maxx, curr)
        else:
            curr = 1
    
    print(maxx)
