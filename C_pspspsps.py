t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    if 'p' in s[:-1] and 's' in s[1:]:
        print("NO")
    else:
        print("YES")