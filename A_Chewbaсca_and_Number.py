x = str(int(input()))
ans = ""
if  int(x[0]) == 9:
    ans += "9"
elif int(x[0]) > 4:
    ans += str(9 - int(x[0]))

else:
    ans += str(int(x[0]))

for v in x[1:]:
    if int(v) > 4 :
        v = str(9 - int(v))
    ans += v
print(ans)