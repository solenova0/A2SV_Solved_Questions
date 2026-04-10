def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        seen = [False] * 26
        kept = 0

        for c in s:
            idx = ord(c) - ord('a')

            if seen[idx]:
                kept += 2
                seen = [False] * 26
            else:
                seen[idx] = True

        print(len(s) - kept)
solve()