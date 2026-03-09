n, B = map(int, input().split())
a = list(map(int, input().split()))
odd = 0
even = 0
cost = []
for i in range(n-1):
    if a[i] % 2 == 0:
        even += 1
    else:
        odd += 1

    if odd == even:
        cost.append(abs(a[i] - a[i+1]))
cost.sort()
cut = 0
total = 0

for c in cost:
    if total + c <= B:
        total += c
        cut += 1
    else:
        break
print(cut)