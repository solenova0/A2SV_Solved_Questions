t = int(input())
for _ in range(t):
    a , b , c  = map(int, input().split())   
    sorted_list = sorted([a, b, c])
    print(min(sorted_list[1] - sorted_list[0], sorted_list[2] - sorted_list[1]))