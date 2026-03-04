from collections import Counter

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    
    freq = Counter(s)
    
    if len(freq) == 1:
        print("NO")
    elif n % 2 == 1:
        mid = n // 2
        v = s[:mid]
        if len(set(v)) == 1 and s[mid] != v[0]:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
        