# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        freq = {}
        root = {}

        for parent, child, isLeft in descriptions:

            if parent not in freq:
                freq[parent] = TreeNode(parent)

            if child not in freq:
                freq[child] = TreeNode(child)

            if isLeft == 1:
                freq[parent].left = freq[child]
            else:
                freq[parent].right = freq[child]

            if root.get(parent, 0) != -1:
                root[parent] = 1

            root[child] = -1

        root_val = 0

        for node, state in root.items():
            if state == 1:
                root_val = node
                break

        return freq[root_val]