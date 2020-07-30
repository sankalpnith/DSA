# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        pre_order = []
        traversal_stack = []
        if root:
            traversal_stack.append(root)
            while traversal_stack:
                node = traversal_stack.pop()
                if node.val:
                    pre_order.append(node.val)
                if node.right:
                    traversal_stack.append(node.right)
                if node.left:
                    traversal_stack.append(node.left)
        return pre_order
