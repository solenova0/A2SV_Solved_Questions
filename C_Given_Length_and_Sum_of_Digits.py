m, s = map(int, input().split())
if m == 1 and s == 0:
    print(0, 0)
elif s == 0 or s > 9 * m:
    print(-1, -1)
else:
    max_ = "9" * (s // 9) + str(s % 9) + "0" * (m - s // 9 - 1)
    min_ = [0] * (m - (s - 1) // 9 - 1) + [(s - 1) % 9] + [9] * ((s - 1) // 9)
    min_[0] += 1
    print("".join(map(str, min_)), max_[:m])