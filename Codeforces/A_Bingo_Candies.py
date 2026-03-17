t = int(input())
for _ in range(t):
    n = int(input())
    freq = {}
    
    for _ in range(n):
        row = list(map(int, input().split()))
        for x in row:
            freq[x] = freq.get(x, 0) + 1
    flag = True
    for v in freq.values():
        if v > n * (n - 1):
            flag = False
            break
    
    print("YES" if flag else "NO")