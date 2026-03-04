import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    i = 0
    possible = True
    
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        
        found = False
        for k in range(i, j):
            if p[k] == a[i]:
                found = True
                break
        
        if not found:
            possible = False
            break
        
        i = j
    
    print("YES" if possible else "NO")