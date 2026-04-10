t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = (pref[i] + a[i]) 
    total = pref[n]
    
    for _ in range(q):
        l, r, k = map(int, input().split())
        
        sub = (pref[r] - pref[l - 1])
        length = r - l + 1
        
        parity = total - sub + length * k
        
        if parity % 2 == 1:
            print("YES")
        else:
            print("NO")