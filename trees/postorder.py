    def postorderTraversal(self, root: TreeNode) -> List[int]:
        s1=[]
        s2=[]
        if root:
            s1.append(root)
        while s1:
            node = s1.pop()
            s2.append(node.val)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        return s2[::-1]
