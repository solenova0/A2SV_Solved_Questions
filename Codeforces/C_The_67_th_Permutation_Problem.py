t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    left = 1
    right = 3 * n
    for _ in range(n):
        res.append(left)        
        res.append(right - 1)    
        res.append(right)      
        left += 1
        right -= 2
    print(*res)