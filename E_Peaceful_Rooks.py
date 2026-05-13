for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[-1, -1] for _ in range(m)]
    row = [-1] * (n + 1)
    col = [-1] * (n + 1)
    visited = [0] * m
    for i in range(m):
        x, y = map(int, input().split())
        if x == y: 
            visited[i] = 1
            continue
        if row[y] != -1:
            graph[row[y]][0]  = i
            graph[i][1] = row[y]
        if col[x] != -1:
            graph[col[x]][1] = i
            graph[i][0] = col[x]
        row[x] = i
        col[y] = i
    # print(graph)
    def dfs(start):
        cycle = 0
        stack = [(start, -1)]
        cnt = 0
        while stack:
            node, par = stack.pop()
            if visited[node]: continue
            cnt += 1
            visited[node] = 1
            curr = 0
            for child in graph[node]:
                if par == 1 - curr or child == -1: 
                    curr += 1
                    continue
                if visited[child]:
                    cycle = 1
                    continue
                stack.append((child, curr))
                curr += 1
        
        return cnt + cycle
    
    ans = 0
    for i in range(m):
        if not visited[i]:
            ans += dfs(i)
    print(ans)
