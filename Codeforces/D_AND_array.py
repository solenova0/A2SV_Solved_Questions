from math import comb


t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    # Array to hold how many numbers should have each bit
    c = [0] * 29  # 0..28
    
    # For each bit position
    for bit in range(29):
        # Determine count of numbers that must have this bit set
        count = 0
        for k in range(n):
            if (b[k] >> bit) & 1:
                count += 1
        c[bit] = count
    
    # Construct array a
    a = [0] * n
    for bit in range(29):
        for i in range(c[bit]):
            a[i] |= (1 << bit)
    
    # Print the result
    print(" ".join(map(str, a)))