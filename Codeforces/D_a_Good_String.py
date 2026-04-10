def solve(s, l, r, c):
    if l == r:
        return 0 if s[l] == c else 1
    
    mid = (l + r) // 2
    left_cost = sum(1 for i in range(l, mid + 1) if s[i] != c)
    right_cost = sum(1 for i in range(mid + 1, r + 1) if s[i] != c)
    
    op1 = left_cost + solve(s, mid + 1, r, chr(ord(c) + 1))
    
    op2 = right_cost + solve(s, l, mid, chr(ord(c) + 1))
    
    return min(op1, op2)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    print(solve(s, 0, n - 1, 'a'))