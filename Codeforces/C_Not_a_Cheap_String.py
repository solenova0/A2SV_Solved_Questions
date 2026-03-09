t = int(input())
for _ in range(t):
    w = input().strip()
    p = int(input())
    price = [ord(c) - 96 for c in w]
    summ = sum(price)

    cnt = [0]*26
    for c in w:
        cnt[ord(c)-97] += 1

    removed = [0]*26

    if summ > p:
        for i in range(25, -1, -1):
            while cnt[i] > 0 and summ > p:
                summ -= (i+1)
                cnt[i] -= 1
                removed[i] += 1
    ans = []
    for c in w:
        idx = ord(c)-97
        if removed[idx] > 0:
            removed[idx] -= 1
        else:
            ans.append(c)

    print("".join(ans))