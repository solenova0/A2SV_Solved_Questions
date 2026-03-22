from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if m > n:
        print("NO")
        continue
    q = deque([n])
    flag = False
    
    while q:
        x = q.popleft()
        if x == m:
            flag = True
            break
        if x < m:
            continue
        if x % 3 == 0:
            q.append(x // 3)
            q.append(2 * (x // 3))
    
    print("YES" if flag else "NO")