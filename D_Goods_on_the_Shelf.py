from random import randint
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    rand = randint(1, 100000)

    def checker(idx1, idx2):
        if idx1 < 0 or idx1 >= n or idx2 < 0 or idx2 >= n:
            return False

        a[idx1], a[idx2] = a[idx2], a[idx1]

        befit = {}

        for i in range(n):
            x = a[i] ^ rand

            if x in befit:
                if befit[x] != i - 1:
                    a[idx1], a[idx2] = a[idx2], a[idx1]
                    return False

            befit[x] = i

        a[idx1], a[idx2] = a[idx2], a[idx1]
        return True

    prev = {}
    for i in range(n):
        x = a[i] ^ rand

        if x in prev:
            if prev[x] != i - 1:

                if checker(prev[x], i - 1):
                    print("YES")
                    return

                if checker(prev[x] + 1, i):
                    print("YES")
                    return

                j1 = prev[x]

                while j1 >= 0 and a[j1] == a[i]:
                    j1 -= 1

                if checker(j1, i):
                    print("YES")
                    return

                j1 += 1

                if checker(j1, i - 1):
                    print("YES")
                    return

                j = n - 1

                while j > i and a[j] != a[i]:
                    j -= 1

                if checker(j, i - 1):
                    print("YES")
                    return

                j2 = i

                while j2 < n - 1 and a[j2] == a[i]:
                    j2 += 1

                if checker(j2, prev[x]):
                    print("YES")
                    return

                print("NO")
                return

        prev[x] = i
    print("YES")
t = int(input())
for _ in range(t):
    solve()