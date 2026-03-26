# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def myFun(root, parent, Gparent):
            if not root:
                return
            if Gparent and Gparent.val % 2 == 0:
                self.ans += root.val
            
            myFun(root.left, root, parent)
            myFun(root.right, root, parent)

        myFun(root, None, None)
        return self.ans