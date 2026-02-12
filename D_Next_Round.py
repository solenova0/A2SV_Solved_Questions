n , k = map(int, input().split())
scores = list(map(int, input().split()))

for i in range(k +1):
    if scores[i] > 0:
        continue
for j in range(k ,n):
    if scores[j] == scores[i] and scores[j] != 0:
        i += 1
print(i)  
