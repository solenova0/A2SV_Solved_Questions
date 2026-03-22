t = int(input())
for _ in range(t):
    r, g, b = map(int, input().split())
    cnt = {'R': r, 'G': g, 'B': b}
    
    s = []
    
    while True:
        colors = sorted(['R', 'G', 'B'], key=lambda x: -cnt[x])
        flag = False
        
        for c in colors:
            if cnt[c] == 0:
                continue
            
            if len(s) >= 1 and s[-1] == c:
                continue
            if len(s) >= 3 and s[-3] == c:
                continue
            s.append(c)
            cnt[c] -= 1
            flag = True
            break
        
        if not flag:
            break
    
    print(''.join(s))