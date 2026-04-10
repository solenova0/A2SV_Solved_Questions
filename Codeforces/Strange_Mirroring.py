def toggle(c):
    if c.islower():
        return c.upper()
    return c.lower()

t = int(input())

for _ in range(t):
    s = input()
    q = int(input())
    queries = list(map(int, input().split()))
    n = len(s)
    
    for k in queries:
        reverse = False
        length = n
        
        while length < k:
            length *= 2
        
        while k > n:
            half = length // 2
            if k > half:
                k -= half
                reverse = not reverse
            length = half
        ch = s[k - 1]
        if reverse:
            ch = toggle(ch)
        
        print(ch, end=' ')
    
    print()