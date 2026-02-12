t = int(input())
for _ in range(t):
    n = int(input())
    full = n // 15
    rem = n % 15
    
    result = 3 * full + min(3,rem +1)
    print(result)


   