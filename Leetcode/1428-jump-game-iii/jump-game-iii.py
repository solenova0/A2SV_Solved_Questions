class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # n = len(arr)
        # q = deque([start])   # BFS
        # visited = set([start])

        # while q:
        #     i = q.popleft()

        #     if arr[i] == 0:
        #         return True

        #     for nxt in (i + arr[i], i - arr[i]):
        #         if 0 <= nxt < n and nxt not in visited:
        #             visited.add(nxt)
        #             q.append(nxt)

        # return False
        n = len(arr)
        visited = set()

        def dfs(i):
            if i < 0 or i >= n or i in visited:
                return False

            if arr[i] == 0:
                return True

            visited.add(i)

            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)