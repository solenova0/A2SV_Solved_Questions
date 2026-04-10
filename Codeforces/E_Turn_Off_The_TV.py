n = int(input())
segments = []

coords = set()

for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r, i + 1))
    coords.add(l)
    coords.add(r)
    coords.add(r + 1)  

coords = sorted(coords)
comp = {x: i for i, x in enumerate(coords)}

diff = [0] * (len(coords) + 1)

for l, r, _ in segments:
    diff[comp[l]] += 1
    diff[comp[r + 1]] -= 1

cover = [0] * len(coords)
cover[0] = diff[0]

for i in range(1, len(coords)):
    cover[i] = cover[i - 1] + diff[i]

is_one = [0] * len(coords)
for i in range(len(coords)):
    if cover[i] == 1:
        is_one[i] = 1

pref = [0] * (len(coords) + 1)
for i in range(len(coords)):
    pref[i + 1] = pref[i] + is_one[i]

for l, r, idx in segments:
    left = comp[l]
    right = comp[r]

    if pref[right + 1] - pref[left] == 0:
        print(idx)
        exit()

print(-1)