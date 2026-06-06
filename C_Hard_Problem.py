for _ in range(int(input())):
    m , a , b , c = map(int, input().split())
    res = 0
    row1 , row2 = 0 , 0
    if a > m:
        res += m
    else :
        res += a
        row1 = m - a

    if b > m:
        res += m
    else :
        res += b
        row2 = m - b
    

    res += min(row1 + row2 , c) 
    print(res)