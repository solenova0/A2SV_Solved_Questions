class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = [0]   

        def dfs(node):
            if node == len(graph) - 1:
                res.append(path[:])  
                return

            for nei in graph[node]:
                path.append(nei)     
                dfs(nei)              
                path.pop()           

        dfs(0)
        return res