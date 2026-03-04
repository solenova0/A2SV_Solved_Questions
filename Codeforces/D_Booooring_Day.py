t = int(input()) 
for _ in range(t):
    n, l, r = map(int, input().split())  
    a = list(map(int, input().split()))  
    
    ans = 0
    curr = 0
    i = 0
    for end in range(n):
        curr += a[end]

        while curr > r and i <= end:
            curr -= a[i]
            i += 1

        if l <= curr <= r:
            ans += 1
            curr = 0
            i = end + 1

    print(ans)  