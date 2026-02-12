def solve():
    s = input()
    t = input()
    p = input()

    i, j = 0, 0  
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1  

    if i != len(s):
        print("NO")
        return

    ferq_t = {}
    for char in t:
        ferq_t[char] = ferq_t.get(char, 0) + 1

    sp = {}
    for char in s + p:
        sp[char] = sp.get(char, 0) + 1

    for char, required_count in ferq_t.items():
        available_count = sp.get(char, 0)
        if required_count > available_count:
            print("NO")
            return

    print("YES")


q = int(input())  
for _ in range(q):
    solve()