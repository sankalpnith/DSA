# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        traversal_stack = []
        if not root:
            return traversal_stack
        current_node = root
        while True:
            if current_node:
                traversal_stack.append(current_node)
                current_node = current_node.left
            elif traversal_stack:
                current_node = traversal_stack.pop()
                inorder.append(current_node.val)
                current_node = current_node.right
            else:
                break
        return inorder
