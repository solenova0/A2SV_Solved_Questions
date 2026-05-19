for _ in range(int(input())):
    k, a , b = map(int, input().split())
    price = (k //2 * min(b , 2*a))+ (k % 2) * a
    print(price)
