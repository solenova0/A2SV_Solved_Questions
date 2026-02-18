t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    i = 0 
    j = 2

    while j < n:
        if s[i:j] in s[j:]:
            print("YES")
            break
        i += 1
        j += 1
    else:
        print("NO")
