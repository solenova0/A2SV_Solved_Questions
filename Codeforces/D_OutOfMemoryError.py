t = int(input())
for _ in range(t):
    n, m, h = map(int, input().split())
    arr = list(map(int, input().split()))
    
    curr = arr[:]
    v = [0] * n
    _v = 0
    
    for _ in range(m):
        b, c = map(int, input().split())
        b -= 1
        
        if v[b] != _v:
            curr[b] = arr[b]
            v[b] = _v
        
        curr[b] += c
        
        if curr[b] > h:
            _v += 1
    
    ans = []
    for i in range(n):
        if v[i] != _v:
            ans.append(arr[i])
        else:
            ans.append(curr[i])
    
    print(*ans)