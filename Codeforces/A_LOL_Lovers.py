n = int(input())
s = input()
l = s.count('L')
o = s.count('O')
L1 = 0
O1 = 0

for k in range(1, n):
    if s[k - 1] == 'L':
        L1 += 1
    else:
        O1 += 1

    if 2 * L1 != l and 2 * O1 != o:
        print(k)
        break
else:
    print(-1)