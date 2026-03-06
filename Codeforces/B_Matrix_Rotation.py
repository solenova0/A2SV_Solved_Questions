t = int(input())
def beautiful(a):
    return a[0][0] < a[0][1] and a[1][0] < a[1][1] and a[0][0] < a[1][0] and a[0][1] < a[1][1]

def rotate(a):
    return [[a[1][0], a[0][0]],
            [a[1][1], a[0][1]]]

for _ in range(t):
    a = [list(map(int, input().split())) for _ in range(2)]

    ok = False
    for _ in range(4):
        if beautiful(a):
            ok = True
            break
        a = rotate(a)

    print("YES" if ok else "NO")