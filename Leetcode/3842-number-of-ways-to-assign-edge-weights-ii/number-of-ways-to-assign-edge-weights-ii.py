class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        LOG = 17

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        depth = [0] * (n + 1)
        parent = [[-1] * (n + 1) for _ in range(LOG)]

        stack = [(1, -1)]
        while stack:
            u, p = stack.pop()
            parent[0][u] = p

            for v in g[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                stack.append((v, u))

        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            a = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[a]

            ans.append(pow(2, d - 1, 1000000007))

        return ans