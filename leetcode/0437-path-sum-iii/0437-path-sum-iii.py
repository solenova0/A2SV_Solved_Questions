# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr):
            if not node:
                return 0

            curr += node.val
            count = pre.get(curr - targetSum, 0)

            pre[curr] = pre.get(curr, 0) + 1
            count += dfs(node.left, curr)
            count += dfs(node.right, curr)
            pre[curr] -= 1

            return count

        pre = {0: 1}
        return dfs(root, 0)