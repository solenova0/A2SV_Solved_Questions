a = input()
b = input()
res = ""
for i in range(len(b)):
    if a[i] == b[i]:
        res = res + '0'
    else:
        res = res + '1'
print(res)