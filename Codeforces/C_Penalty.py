t = int(input())
for _ in range(t):
    s = input().strip()
    ans = 9

    cnt0 = 0
    cnt1 = 0
    for i in range(10):
        if i % 2 == 0:
            cnt0 += (s[i] != '0')  
        else:
            cnt1 += (s[i] == '1')


        if cnt0 > cnt1 + (10 - i) // 2:
            ans = min(ans, i)
        if cnt1 > cnt0 + (9 - i) // 2:
            ans = min(ans, i)
            
    cnt0 = 0
    cnt1 = 0
    for i in range(10):
        if i % 2 == 0:
            cnt0 += (s[i] == '1')
        else:
            cnt1 += (s[i] != '0')  

        if cnt0 > cnt1 + (10 - i) // 2:
            ans = min(ans, i)
        if cnt1 > cnt0 + (9 - i) // 2:
            ans = min(ans, i)

    print(ans + 1)