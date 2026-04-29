class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
        
        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited
        result = []
        
        def dfs(node):
            if visited[node] == 1:
                return False  # cycle
            if visited[node] == 2:
                return True
            
            visited[node] = 1
            
            for v in graph[node]:
                if not dfs(v):
                    return False
            
            visited[node] = 2
            result.append(node)
            return True
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        
        return result[::-1]