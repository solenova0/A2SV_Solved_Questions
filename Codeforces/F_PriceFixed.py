n = int(input())
p = []
for _ in range(n):
    a, b = map(int, input().split())
    p.append([b, a]) 

p.sort()  
total = 0
cost = 0
i = 0
j = n - 1

while i <= j:
    if total >= p[i][0]:
        cost += p[i][1]  
        total += p[i][1]
        i += 1
    else:
        need = p[i][0] - total
        take = min(need, p[j][1])
        cost += 2 * take
        total += take
        p[j][1] -= take
        if p[j][1] == 0:
            j -= 1

print(cost)