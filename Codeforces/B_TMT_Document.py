t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    if s.count('T') != 2 * s.count('M'):
        print("NO")
        continue

    balance = 0
    flag = True
    for c in s:
        balance += 1 if c == 'T' else -1
        if balance < 0:
            flag = False

    balance = 0
    for c in s[::-1]:
        balance += 1 if c == 'T' else -1
        if balance < 0:
            flag = False

    print("YES" if flag else "NO")