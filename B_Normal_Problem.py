for _ in range(int(input())):
    a = input()
    b = []
    for i in range(len(a)):
        if a[i] == "p":
            b.append("q")
        elif a[i] == "q":
            b.append("p")
        else:
            b.append(a[i])
    b = b[::-1] 
    print(''.join(b))