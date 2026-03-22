n = int(input())
s = input().strip()
res = []

for ch in s:
    if len(res) % 2 == 0:
        res.append(ch)
    else:
        if res[-1] != ch:
            res.append(ch)

if len(res) % 2 != 0:
    res.pop()

print(n - len(res))
print("".join(res))