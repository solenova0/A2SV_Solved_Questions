n = int(input())
a = list(map(int,input().split()))
a.sort()

count = 1
for v in a:
    if v >= count:
        count += 1
print(count -)
