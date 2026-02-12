r = c = 0
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            r, c = i + 1, j + 1

print(abs(r - 3) + abs(c - 3))
