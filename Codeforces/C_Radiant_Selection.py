import math
t = int(input())
for _ in range(t):
    k = int(input())
        
    left, right = 1, 10**18 + math.isqrt(10**18)
    while left < right:
        mid = (left + right) // 2
        if mid - int(math.isqrt(mid) )>= k:
            right = mid
        else:
            left = mid + 1
        
    print(left)

