t = int(input())  
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))  
    sorted_a = sorted(a)  
    
    visited = [False] * n  
    valid = True  

    for i in range(n):
        if not visited[i]:
            v = []
            curr = i + 1  
            while curr <= n:
                idx = curr - 1
                v.append(idx)
                visited[idx] = True
                curr *= 2

            current = [a[idx] for idx in v]
            target = [sorted_a[idx] for idx in v]

            if sorted(current) != sorted(target):
                valid = False
                break

    if valid:
        print("YES")
    else:
        print("NO")
