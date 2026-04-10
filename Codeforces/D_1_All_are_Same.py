# import math

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
    
#     arr.sort()
#     g = 0
    
#     for i in range(1, n):
#         g = math.gcd(g, arr[i] - arr[0])
    
#     print(g)

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    # Condition 1
    if s.count('T') != 2 * s.count('M'):
        print("NO")
        continue
    
    # Condition 2 (left to right)
    t_count = 0
    m_count = 0
    ok = True
    
    for c in s:
        if c == 'T':
            t_count += 1
        else:
            m_count += 1
        
        if m_count > t_count:
            ok = False
            break
    
    # Condition 3 (right to left)
    t_count = 0
    m_count = 0
    
    for c in reversed(s):
        if c == 'T':
            t_count += 1
        else:
            m_count += 1
        
        if m_count > t_count:
            ok = False
            break
    
    print("YES" if ok else "NO")