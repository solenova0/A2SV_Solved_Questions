import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = []
    
    for i in range(n):
        for j in range(1, n):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                ans.append((1, j))  
    
    for i in range(n):
        for j in range(1, n):
            if b[j - 1] > b[j]:
                b[j - 1], b[j] = b[j], b[j - 1]
                ans.append((2, j))
    
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]  
            ans.append((3, i + 1))
    
    print(len(ans))
    for x, y in ans:
        print(x, y)