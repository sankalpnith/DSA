def levelOrder(self, root: TreeNode) -> List[int]:
        queue = []
        traversed = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node:
                traversed.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        print(traversed)
	return traversed
