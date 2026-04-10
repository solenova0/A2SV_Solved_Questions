recipe = input().strip()
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())
money = int(input())

cb = recipe.count('B')
cs = recipe.count('S')
cc = recipe.count('C')

def f(x):
    buy_b = max(0, cb * x - nb)
    buy_s = max(0, cs * x - ns)
    buy_c = max(0, cc * x - nc)
    return buy_b * pb + buy_s * ps + buy_c * pc

l, r = 0, 10**13

while l < r:
    mid = (l + r + 1) // 2
    if f(mid) <= money:
        l = mid
    else:
        r = mid - 1

print(l)