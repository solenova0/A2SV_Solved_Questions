import math
n, x0, y0 = map(int, input().split())

lines = set()

for _ in range(n):
    x, y = map(int, input().split())

    dx = x - x0
    dy = y - y0

    g = math.gcd(abs(dx), abs(dy))
    dx //= g
    dy //= g

    if dx < 0 or (dx == 0 and dy < 0):
        dx *= -1
        dy *= -1

    lines.add((dx, dy))

print(len(lines))