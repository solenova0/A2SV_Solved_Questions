# Match what you can for free
# Balance sides smartly
# Use same-color pairs to reduce cost
# Recolor only when necessary
import sys
input = sys.stdin.readline

def solve():
    N, L, R = map(int, input().split())
    C = list(map(int, input().split()))
    
    lcnt = [0] * (N + 1)
    rcnt = [0] * (N + 1)
    
    # Count colors
    for i in range(N):
        if i < L:
            lcnt[C[i]] += 1
        else:
            rcnt[C[i]] += 1
    
    # Remove already matched pairs
    for i in range(1, N + 1):
        mn = min(lcnt[i], rcnt[i])
        lcnt[i] -= mn
        rcnt[i] -= mn
        L -= mn
        R -= mn
    
    # Ensure L >= R
    if L < R:
        lcnt, rcnt = rcnt, lcnt
        L, R = R, L
    
    ans = 0
    
    # Fix imbalance using pairs on left
    for i in range(1, N + 1):
        extra = L - R  # always even
        can_do = lcnt[i] // 2
        Do = min(can_do * 2, extra)
        
        ans += Do // 2
        L -= Do
    
    # Final adjustments
    ans += (L - R) // 2 + (L + R) // 2
    
    print(ans)


t = int(input())
for _ in range(t):
    solve()