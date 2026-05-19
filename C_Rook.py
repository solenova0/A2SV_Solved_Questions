def solve():
        pos = input().strip()
        col = pos[0]
        row = pos[1]

        for r in range(1, 9):
            if str(r) != row:
                print(col + str(r))

        for c in "abcdefgh":
            if c != col:
                print(c + row)
for  _ in range(int(input())):
    solve()