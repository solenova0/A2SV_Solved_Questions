t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = []
    
    for i in range(n):
        greater = 0
        smaller = 0
        
        for j in range(i + 1, n):
            if a[j] > a[i]:
                greater += 1
            elif a[j] < a[i]:
                smaller += 1
        
        ans.append(max(greater, smaller))
    
    print(*ans)