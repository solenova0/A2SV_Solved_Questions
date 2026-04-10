n = int(input())
E = {}
for _ in range(n):
    l, r = map(int, input().split())
    
    E[l] = E.get(l, 0) + 1
    E[r + 1] = E.get(r + 1, 0) - 1
points = sorted(E.keys())
res = [0] * (n + 1)

curr = 0

for i in range(len(points) - 1):
    x = points[i]
    curr += E[x]
    
    next_x = points[i + 1]
    
    length = next_x - x  
    
    if curr > 0:
        res[curr] += length

print(*res[1:])
