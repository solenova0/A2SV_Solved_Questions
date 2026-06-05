from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = Counter()
    for _ in range(n):
        s = input().strip()
        cnt.update(s)
    #print(cnt)
    ok = True

    for freq in cnt.values():
        if freq % n != 0:
            ok = False
            break

    print("YES" if ok else "NO")