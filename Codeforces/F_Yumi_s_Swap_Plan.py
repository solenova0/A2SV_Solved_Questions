n = int(input())
s = input().strip()

H = s.count('H')
T = s.count('T')

v = s + s

w = H
currT = v[:w].count('T')
swap = currT

for i in range(1, n):
    if v[i-1] == 'T':
        currT -= 1
    if v[i + w - 1] == 'T':
        currT += 1
    swap = min(swap, currT)

print(swap)