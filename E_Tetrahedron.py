mod = 1000000007

n = int(input())

d = 1
a = b = c = 0

for _ in range(n):
    nd = (a + b + c) % mod
    na = (d + b + c) % mod
    nb = (d + a + c) % mod
    nc = (d + a + b) % mod
    d, a, b, c = nd, na, nb, nc

print(d)