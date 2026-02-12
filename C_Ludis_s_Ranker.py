n = int(input())
a = list(map(int, input().split()))

rank = []
for i in range(n):
    high = 0
    for j in range(n):
        if a[j] > a[i]:
            high += 1
    rank.append(high + 1)

for i in range(n):
    print(rank[i], end=" ")
