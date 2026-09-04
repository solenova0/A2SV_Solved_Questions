n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos = [0] * (n + 1)

for i, x in enumerate(a):
    pos[x] = i

count = [0] * n

for i, x in enumerate(b):
    shift = (i - pos[x]) % n
    count[shift] += 1

print(max(count))