n = int(input())  
matrix = []  
for _ in range(n):  
    inp = [int(i) for i in input().split()]  
    matrix.append(inp)  

visited = set()  
mid_row = mid_col = n // 2  
ans = 0  

for i in range(n):  
    # Main diagonal  
    if (i, i) not in visited:  
        ans += matrix[i][i]  
        visited.add((i, i))  

    # Secondary diagonal  
    if (i, n - 1 - i) not in visited:  
        ans += matrix[i][n - 1 - i]  
        visited.add((i, n - 1 - i))  

    # Middle row  
    if (mid_row, i) not in visited:  
        ans += matrix[mid_row][i]  
        visited.add((mid_row, i))  

    # Middle column  
    if (i, mid_col) not in visited:  
        ans += matrix[i][mid_col]  
        visited.add((i, mid_col))  

print(ans)