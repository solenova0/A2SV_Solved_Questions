import sys
input = sys.stdin.readline
def solve():
    s = input().strip()
    t = input().strip()

    countT = [0]*26
    for c in t:
        countT[ord(c)-97] += 1

    countS = [0]*26
    for c in s:
        countS[ord(c)-97] += 1

    for i in range(26):
        if countT[i] < countS[i]:
            print("Impossible")
            return
    result = []
    s_idx = 0
    n = len(t)
    m = len(s)

    for _ in range(n):
        for c in range(26):
            if countT[c] == 0:
                continue
            can_take = False
            ch = chr(c + 97)

            if s_idx < m and ch == s[s_idx]:
                can_take = True
            else:
                countT[c] -= 1
                possible = True
                for j in range(26):
                    if countT[j] < countS[j]:
                        possible = False
                        break
                if possible:
                    can_take = True
                countT[c] += 1

            if can_take:
                result.append(ch)
                countT[c] -= 1
                if s_idx < m and ch == s[s_idx]:
                    countS[ord(s[s_idx]) - 97] -= 1
                    s_idx += 1
                break

    print("".join(result))
t = int(input())
for _ in range(t):
    solve()