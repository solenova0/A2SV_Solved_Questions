# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_index = {v: i for i, v in enumerate(postorder)}

        def build(preL, preR, postL, postR):
            if preL > preR:
                return None

            root = TreeNode(preorder[preL])

            if preL == preR:
                return root

            left_root_val = preorder[preL + 1]
            idx = post_index[left_root_val]

            left_size = idx - postL + 1

            root.left = build(preL + 1, preL + left_size, postL, idx)
            root.right = build(preL + left_size + 1, preR, idx + 1, postR - 1)

            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)