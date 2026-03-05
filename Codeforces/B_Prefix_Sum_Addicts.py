t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    if k == 1:
        print("YES")
        continue
    
    d = []
    for i in range(1, k):
        d.append(s[i] - s[i - 1])
    
    flag = True
    for i in range(1, len(d)):
        if d[i] < d[i - 1]:
            flag = False
            break
    
    if not flag:
        print(" No")
        continue
    
    needed = s[0]
    max_sum = d[0] * (n - k + 1)
    
    if max_sum < needed:
        print("No")
    else:
        print("Yes")