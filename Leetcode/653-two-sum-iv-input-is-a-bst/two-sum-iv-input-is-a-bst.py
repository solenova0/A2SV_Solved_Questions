# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node):
            if not node:
                return False
            
            return (
                dfs(node.left) or
                dfs(node.right) or
                search(root, k - node.val, node)
            )
        
        def search(node, target, skip):
            if not node:
                return False
            
            if node != skip and node.val == target:
                return True
            
            return search(node.left, target, skip) or search(node.right, target, skip)
        
        return dfs(root)