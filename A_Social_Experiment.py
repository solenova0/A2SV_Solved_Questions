t = int(input())

for _ in range(t):
    n = int(input())

    if n < 4:
        print(n)
    elif n % 4 == 0:
        print(0)
    elif n % 3 == 0 and n % 2 == 0:
        print(0)
    else:   
        print(n % 2)
