n, r, av = map(int, input().split())
exams = []
curr = 0
for _ in range(n):
    a, b = map(int, input().split())
    exams.append((a, b))
    curr += a
need = av * n - curr
if need <= 0:
    print(0)
    exit()
exams.sort(key=lambda x: x[1])

essays = 0
for a, b in exams:
    if need <= 0:
        break
    
    inc = r - a
    take = min(need, inc)
    
    essays += take * b
    need -= take

print(essays)