n, a, b, k = map(int, input().split())
h = list(map(int, input().split()))
cycle = a + b
costs = []
ans = 0

for hp in h:
    hp = (hp - 1) % cycle + 1
    
    if hp <= a:
        ans += 1
    else:
        needed = (hp - 1) // a
        costs.append(needed)

costs.sort()

for c in costs:
    if k >= c:
        k -= c
        ans += 1
    else:
        break

print(ans)