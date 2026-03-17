n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
count = 0
for i in range(n):
    if b[i] != a[i]:
        count += 1
if count > 2 :
    print("NO")
else:
    print("YES")