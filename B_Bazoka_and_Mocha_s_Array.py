t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
#     flag = False
#     for i in range(n):
#         b = a[i:] + a[:i]

#         sorted = True
#         for j in range(n - 1):
#             if b[j] > b[j + 1]:
#                 sorted = False
#                 break

#         if sorted:
#             flag = True
#             break

#     print("Yes" if flag else "No")


    count = 0
    for i in range(n):
        if a[i] > a[(i + 1) % n]:
            count += 1

    print("Yes" if count <= 1 else "No")