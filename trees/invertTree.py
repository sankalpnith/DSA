def invertTree(self, root: TreeNode) -> TreeNode:
        queue = []
        if root:
            queue.append(root)
        while queue:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
def invertTree(self, root):
         if not root:
             return
         self.invertTree(root.left)
         self.invertTree(root.right)
         root.left, root.right = root.right, root.left
         return root
