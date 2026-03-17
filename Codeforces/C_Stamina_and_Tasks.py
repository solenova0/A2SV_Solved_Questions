t = int(input())
for _ in range(t):
    n = int(input())
    T = [tuple(map(int, input().split())) for _ in range(n)]
    best = 0.0
    
    for c, p in reversed(T):
        r = 1 - p / 100.0
        best = max(best, c + r * best)
    
    print(round(best, 10))