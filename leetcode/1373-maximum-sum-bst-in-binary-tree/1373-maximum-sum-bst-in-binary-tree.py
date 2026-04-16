# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:    
        ans = 0
        def dfs(node):
            nonlocal ans
            
            if not node:
                return (True, float('inf'), float('-inf'), 0)
            
            l_bst, l_min, l_max, l_sum = dfs(node.left)
            r_bst, r_min, r_max, r_sum = dfs(node.right)
            if l_bst and r_bst and l_max < node.val < r_min:
                s = l_sum + r_sum + node.val
                ans = max(ans, s)
                
                return (True,
                        min(l_min, node.val),
                        max(r_max, node.val),
                        s)
            
            return (False, 0, 0, 0)

        dfs(root)
        return ans