 def createPaths(self, root, path, output):
        path = path[:]
        if not root:
            return
        path.append(str(root.val))
        if not (root.left or root.right):
            output.append("->".join(path))
        else:
            self.createPaths(root.left, path, output)
            self.createPaths(root.right, path, output)
        return output  
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path = []
        output = []
        return self.createPaths(root, path, output)
