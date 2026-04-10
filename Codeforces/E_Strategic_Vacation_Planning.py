import bisect
n, x = map(int, input().split())
vi = []
for _ in range(n):
    l, r, c = map(int, input().split())
    vi.append((l, r, r - l + 1, c))

vi.sort()
vf = sorted(vi, key=lambda v: v[1])
ends = [v[1] for v in vf]

dur = {}  
ans = float('inf')

processed = 0 

for l, r, dur_i, cost_i in vi:
    pos = bisect.bisect_left(ends, l)
    while processed < pos:
        _, _, d, c = vf[processed]
        if d not in dur or c < dur[d]:
            dur[d] = c
        processed += 1
    need = x - dur_i
    if need in dur:
        ans = min(ans, cost_i + dur[need])

print(ans if ans != float('inf') else -1)