import sys
input = sys.stdin.read

data = input().split()
p = 0

t = int(data[p])
p += 1

res = []

for _ in range(t):
    n = int(data[p]); p += 1
    m = int(data[p]); p += 1
    h = int(data[p]); p += 1
    
    a = list(map(int, data[p : p + n]))
    p += n
    
    ops = []
    for _ in range(m):
        b = int(data[p]) - 1  
        c = int(data[p + 1])
        p += 2
        ops.append((b, c))
    
    delta = [0] * n
    last_reset = -1
    
    for i in range(m):
        idx, c = ops[i]
        if a[idx] + delta[idx] + c > h:
            delta = [0] * n
            last_reset = i
        else:
            delta[idx] += c
    
    final_a = a[:]
    for i in range(last_reset + 1, m):
        idx, c = ops[i]
        final_a[idx] += c
    
    res.append(" ".join(map(str, final_a)))

print("\n".join(res))
