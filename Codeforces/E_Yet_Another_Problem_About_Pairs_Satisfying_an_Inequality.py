t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    pref = [0]*(n+1)
    ans = 0
    for i in range(1,n+1):
        pref[i] = pref[i-1]
        
        if a[i] < i:
            ans += pref[a[i]-1] if a[i]-1 >= 0 else 0
            pref[i] += 1
    
    print(ans)